import sys
import struct
import yaml
from pathlib import Path
import opcode_defs
import chars
import file_crypt

UNITS = {}

def dump_units(script):
    unit_def = [
        {"name":"id", "type":"I" },
        {"name":"force", "type":"i" },
        {"name":"unk08", "type":"I" },
        {"name":"unk0C", "type":"I" },
        {"name":"unk10", "type":"I" },
        {"name":"x", "type":"I" },
        {"name":"y", "type":"I" },
        {"name":"unk1C", "type":"I" },
        {"name":"unk20", "type":"I" },
        {"name":"unk24", "type":"I" },
        {"name":"unk28", "type":"I" },
        {"name":"unk2C", "type":"I" },
        {"name":"unk30", "type":"I" },
        {"name":"unk34", "type":"I" },
        {"name":"unk38", "type":"I" },
        {"name":"inactive", "type":"I" },
        {"name":"unk40", "type":"I" },
        {"name":"unk44", "type":"I" },
        {"name":"unk48", "type":"I" },
    ]
    
    out_data = {}

    units_offset, units_size = struct.unpack_from("<II", script, 0xC)

    pos = units_offset
    num = 0
    while pos < units_offset + units_size:
        out_data[f"0x{num:X}"] = {}

        for d in unit_def:
            val = struct.unpack_from(f"<{d['type']}", script, pos)[0]
            pos += 4

            if d["name"] == "id":
                char_name = chars.char_id_to_name(val)
                out_data[f"0x{num:X}"][d["name"]] = f"0x{val:X} ({char_name})"

                UNITS[num] = char_name
            else:
                match d["type"]:
                    case "I":
                        out_data[f"0x{num:X}"][d["name"]] = f"0x{val:X}"
                    case "i":
                        out_data[f"0x{num:X}"][d["name"]] = val
                    case _:
                        print(f"Unhandled unit type {d['type']}")
                        exit()

        num += 1

    print(f"Decompiled {sys.argv[1]}_units.yaml")

    with open(sys.argv[1] + "_units.yaml", "w") as f:
        f.write(yaml.dump(out_data, sort_keys=False))

def dump_script(script):
    def decompile_conditions(script, pos, out_script, op1, simplified_condition):
        opcode = struct.unpack_from("<I", script, pos)[0]
        opcode_data = opcode_defs.OPCODES_CONDITIONS[opcode]
        opcode_name = opcode_data["name"]
        opcode_size = opcode_data["size"]

        opcode_handler = opcode_defs.HANDLERS_CONDITIONS[opcode]

        args = opcode_handler.decompile(script, pos + 0x4, UNITS)

        new_script = {}
        new_script["opcode"] = opcode_name
        new_script["index"] = op1
        new_script["args"] = args

        pos += opcode_data["size"] * 4

        if opcode_name == "and" or opcode_name == "or":
            new_script["opcodes"] = []

            count = args["num_args"]
            condition = "&&" if opcode_name == "and" else "||"
            base_op1 = op1

            if count > 1:
                simplified_condition += f"("

            for i in range(count):
                pos, simplified_condition, op1 = decompile_conditions(script, pos, new_script["opcodes"], op1 + 1, simplified_condition)
                if i + 1 < count:
                    simplified_condition += f" {condition} "

            if count > 1:
                simplified_condition += f")"

            out_script.append(new_script)

        else:
            out_script.append(new_script)
            simplified_condition += f"{op1}"

        return pos, simplified_condition, op1

    out_data = {}

    script_offset, script_size = struct.unpack_from("<II", script, 0x74)

    script_entry_count = struct.unpack_from("<I", script, script_offset)[0]
    script_hdr_size = struct.unpack_from("<I", script, script_offset + 0x18)[0]

    script_table = script_offset + script_hdr_size
    #print(f"table 0x{script_table:X}")
    for entry in range(script_entry_count):
        offset = struct.unpack_from("<I", script, script_table + entry * 4)[0]
        #print(f"0x{offset:X}")

        entry_offset = script_offset + offset

        entry_hdr_size = struct.unpack_from(f"<I", script, entry_offset + 0x18)[0] - offset

        entry_info = struct.unpack_from(f"<{entry_hdr_size // 4}I", script, entry_offset)

        #print(f"Entry {entry_info[0]} at 0x{entry_offset:X}")
        out_data[entry_info[0]] = {}

        out_data[entry_info[0]]["info"] = {}
        off = 0x4
        for data in entry_info[1:]:
            if off == 0x18:
                out_data[entry_info[0]]["info"]["conditions_offset"] = f"0x{data + script_offset:X}"
            elif off == 0x1C:
                out_data[entry_info[0]]["info"]["conditions2_offset"] = f"0x{data + script_offset:X}"
            elif off == 0x20:
                out_data[entry_info[0]]["info"]["num_script_opcodes"] = f"{data}"
            elif off == 0x24:
                out_data[entry_info[0]]["info"]["script_offset"] = f"0x{data + script_offset:X}"
            elif off == 0x2C:
                out_data[entry_info[0]]["info"]["end_offset"] = f"0x{data + script_offset:X}"
            else:
                out_data[entry_info[0]]["info"][f"unk{off:02X}"] = f"0x{data:X}"
            off += 4

        out_data[entry_info[0]]["conditions"] = []
        pos = script_offset + entry_info[6]
        simple_cond = ""
        while pos < script_offset + entry_info[7]:
            pos, simple_cond, op1 = decompile_conditions(script, pos, out_data[entry_info[0]]["conditions"], 0, "")

        out_data[entry_info[0]]["info"]["condition1"] = simple_cond

        out_data[entry_info[0]]["conditions2"] = []
        pos = script_offset + entry_info[7]
        simple_cond = ""
        while pos < script_offset + entry_info[9]:
            pos, simple_cond, op1 = decompile_conditions(script, pos, out_data[entry_info[0]]["conditions2"], 0, "")
        
        out_data[entry_info[0]]["info"]["condition2"] = simple_cond

        out_data[entry_info[0]]["script"] = []
        pos = script_offset + entry_info[9]
        for op3 in range(entry_info[8]):
            opcode = struct.unpack_from("<I", script, pos)[0]
            opcode_data = opcode_defs.OPCODES_SCRIPT[opcode]
            opcode_name = opcode_data["name"]
            opcode_size = opcode_data["size"]

            opcode_handler = opcode_defs.HANDLERS_SCRIPT[opcode]

            out_opcode = {}
            out_opcode["opcode"] = opcode_name
            out_opcode["args"] = opcode_handler.decompile(script, pos + 0x4, UNITS)

            out_data[entry_info[0]]["script"].append(out_opcode)

            pos += opcode_size * 4

    print(f"Decompiled {sys.argv[1]}_script.yaml")

    with open(sys.argv[1] + "_script.yaml", "w") as f:
        f.write(yaml.dump(out_data, sort_keys=False))

orig_path = Path("LINKDATA_EX_TRIAL.BIN.orig")
if not orig_path.is_file():
    fd = Path("LINKDATA_EX_TRIAL.BIN").read_bytes()
    orig_path.write_bytes(fd)
    del fd

if sys.argv[1] == "orig":
    linkdata = orig_path.read_bytes()
    offset, size = struct.unpack_from("<2Q", linkdata, 0x10 + 1 * 0x10)
    script = linkdata[offset * 0x100: offset * 0x100 + size]
    script = file_crypt.crypt(script, "dec")
else:
    stage_idx = int(sys.argv[1])
    if stage_idx not in range(1194, 1384 + 1):
        print(f"Invalid stage index, index must be between 1194 and 1384")
        exit()

    f_path = Path.cwd().parent.parent / "LINKDATA_A"
    if not f_path.exists():
        print(f"Could not find \"{f_path}\".\nMake sure LINKDATA_A has been extracted, and you're running this script from inside /EX/TRIAL")
        exit()

    f_path = f_path / f"{stage_idx}"
    if not f_path.exists():
        print(f"Could not find \"{f_path}\".\nMake sure LINKDATA_A has been extracted, and you're running this script from inside /EX/TRIAL")
        exit()

    script = f_path.read_bytes()

dump_units(script)
dump_script(script)
