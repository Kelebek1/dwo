import sys
import struct
import opcode_defs
import yaml
from pathlib import Path
from chars import CHARS
import file_crypt

DUMP_COMPILED_SCRIPT = True
DUMP_COMPILED_SCRIPT_ENCRYPTED = False

UNITS = {}

def build_units(data):
    out_data = []

    for id, unit in data.items():
        for name, v in unit.items():
            if name == "id":
                base_id, char_name = unit["id"].split("(",1)
                UNITS[id] = char_name.split(")",1)[0]
                out_data.append(struct.pack("<I", int(base_id, 16)))
            elif name == "force":
                out_data.append(struct.pack("<i", v))
            else:
                out_data.append(struct.pack("<I", int(v, 16)))

    return b"".join(out_data)

def build_script(data):
    def compile_conditions(script):
        opcodes_conditions = []

        for opcode in script:

            op_info = opcode_defs.OPCODES_CONDITIONS[opcode["opcode"]]
            op_handler = opcode_defs.HANDLERS_CONDITIONS[op_info["id"]]

            opcodes_conditions.append(struct.pack("<I", op_info["id"]))
            opcodes_conditions.append(op_handler.compile(opcode, UNITS))

            if op_info["name"] == "and" or op_info["name"] == "or":
                if "opcodes" not in opcode:
                    opcode["opcodes"] = []
                opcodes_conditions.append(compile_conditions(opcode["opcodes"]))

        return b"".join(opcodes_conditions)

    out_data = []

    num_scripts = len(data)
    curr_offset = 0x30 + num_scripts * 4
    script_offsets = []

    for script_id, script in data.items():
        print(f"Packing script {script_id} at 0x{curr_offset:X}")

        opcodes_conditions = b""
        # Add a default empty "and" condition if it doesn't exist, this is what the game does by default
        if "conditions" not in script:
            script["conditions"] = [{'opcode': 'and', 'index': 0, 'args': {'unk00': '0x0', 'num_args': 0, 'num_dwords': '0x0'}, 'opcodes': []}]
        opcodes_conditions = compile_conditions(script["conditions"])

        opcodes_conditions2 = b""
        if "conditions2" not in script:
            script["conditions2"] = [{'opcode': 'and', 'index': 0, 'args': {'unk00': '0x0', 'num_args': 0, 'num_dwords': '0x0'}, 'opcodes': []}]
        opcodes_conditions2 = compile_conditions(script["conditions2"])

        opcodes_script = []
        num_script_opcodes = 0
        if "script" in script and len(script["script"]) > 0:
            for opcode in script["script"]:
                op_info = opcode_defs.OPCODES_SCRIPT[opcode["opcode"]]
                op_handler = opcode_defs.HANDLERS_SCRIPT[op_info["id"]]

                opcodes_script.append(struct.pack("<I", op_info["id"]))
                opcodes_script.append(op_handler.compile(opcode, UNITS))

                num_script_opcodes += 1

        opcodes_script = b"".join(opcodes_script)

        # Info

        opcodes_conditions_offset = curr_offset
        opcodes_conditions2_offset = curr_offset + len(opcodes_conditions)
        opcodes_script_offset = curr_offset + len(opcodes_conditions) + len(opcodes_conditions2)
        end = curr_offset + len(opcodes_conditions) + len(opcodes_conditions2) + len(opcodes_script)

        script_offsets.append(curr_offset)

        curr_offset = 0x30 + end

        out_data.append(struct.pack("<I", script_id))
        out_data.append(struct.pack("<I", int(script["info"]["unk04"], 16)))
        out_data.append(struct.pack("<I", int(script["info"]["unk08"], 16)))
        out_data.append(struct.pack("<I", int(script["info"]["unk0C"], 16)))
        out_data.append(struct.pack("<I", int(script["info"]["unk10"], 16)))
        out_data.append(struct.pack("<I", int(script["info"]["unk14"], 16)))
        out_data.append(struct.pack("<I", 0x30 + opcodes_conditions_offset))
        out_data.append(struct.pack("<I", 0x30 + opcodes_conditions2_offset))
        out_data.append(struct.pack("<I", num_script_opcodes))
        out_data.append(struct.pack("<I", 0x30 + opcodes_script_offset))
        out_data.append(struct.pack("<I", int(script["info"]["unk28"], 16)))
        out_data.append(struct.pack("<I", 0x30 + end))

        out_data.append(opcodes_conditions)
        out_data.append(opcodes_conditions2)
        out_data.append(opcodes_script)

    out_data = b"".join(out_data)

    header = struct.pack("<I", num_scripts)
    header += struct.pack("<5I", 0, 0, 0, 0, 0)
    header += struct.pack("<I", 0x30)
    for i in range(5):
        header += struct.pack("<I", curr_offset)

    for i in range(num_scripts):
        header += struct.pack("<I", script_offsets[i])

    return header + out_data

#######################################################################################################

#build_offsets()

in_file = Path("LINKDATA_EX_TRIAL.BIN.orig")
out_file = Path("LINKDATA_EX_TRIAL.BIN")

if not in_file.is_file():
    with open("LINKDATA_EX_TRIAL.BIN", "rb") as f:
        fd = f.read()
    with open("LINKDATA_EX_TRIAL.BIN.orig", "wb") as f:
        f.write(fd)
    del fd

with open(in_file, "rb") as f:
    linkdata = f.read()

if sys.argv[1] == "orig":
    offset, size = struct.unpack_from("<QI", linkdata, 0x10 + 1 * 0x10)
    orig_script = linkdata[offset * 0x100:offset * 0x100 + size]
    orig_script = file_crypt.crypt(orig_script, "dec")
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

    with open(f_path, "rb") as f:
        orig_script = f.read()

num_orig_tables = struct.unpack_from("<I", orig_script, 0)[0]
tables = {}

for num_table in range(num_orig_tables):
    table_offset, table_size = struct.unpack_from("<II", orig_script, 4 + num_table * 8)
    table = orig_script[table_offset:table_offset + table_size]
    tables[num_table] = table

with open(sys.argv[1] + "_units.yaml", "r") as f:
    units = yaml.safe_load(f.read())

tables[1] = build_units(units)

with open(sys.argv[1] + "_script.yaml", "r") as f:
    script = yaml.safe_load(f.read())

tables[14] = build_script(script)

out_data = bytes()
out_data += struct.pack("<I", num_orig_tables)

curr_size = 4 + num_orig_tables * 8
for table_num, table in tables.items():
    out_data += struct.pack("<II", curr_size, len(table))
    curr_size += len(table)

for table_num, table in tables.items():
    out_data += table

if DUMP_COMPILED_SCRIPT:
    with open("script_compiled", "wb") as f:
        f.write(out_data)

out_data = file_crypt.crypt(out_data, "enc")

if DUMP_COMPILED_SCRIPT_ENCRYPTED:
    with open("script_compiled_encrypted", "wb") as f:
        f.write(out_data)

#exit()

orig_toc_offset = 0x10 + 1 * 0x10

while len(linkdata) % 0x100:
    linkdata += b"\x00"
offset = len(linkdata) // 0x100
size = len(out_data)

new_linkdata = linkdata[:orig_toc_offset]
new_linkdata += struct.pack("<QII", offset, len(out_data), 0)
new_linkdata += linkdata[orig_toc_offset + 0x10:offset * 0x100]
new_linkdata += out_data

with open(out_file, "wb") as f:
    f.write(new_linkdata)
