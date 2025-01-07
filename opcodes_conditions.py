import struct

OPCODES_CONDITIONS = {
    0x00000000 : {"name":"script_status", "id":0x00000000, "index":0x00, "size":3,
                  "args": { "status":"I", "script_id":"i", }},
    0x0000000A : {"name":"0x0000000A", "id":0x0000000A, "index":0x01, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000014 : {"name":"0x00000014", "id":0x00000014, "index":0x02, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000001E : {"name":"0x0000001E", "id":0x0000001E, "index":0x03, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000082 : {"name":"0x00000082", "id":0x00000082, "index":0x04, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000000B : {"name":"0x0000000B", "id":0x0000000B, "index":0x05, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000015 : {"name":"0x00000015", "id":0x00000015, "index":0x06, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000003E8 : {"name":"0x000003E8", "id":0x000003E8, "index":0x07, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000003F2 : {"name":"0x000003F2", "id":0x000003F2, "index":0x08, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000003F7 : {"name":"0x000003F7", "id":0x000003F7, "index":0x09, "size":7,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x000003FA : {"name":"0x000003FA", "id":0x000003FA, "index":0x0A, "size":8,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", }},
    0x00000528 : {"name":"0x00000528", "id":0x00000528, "index":0x0B, "size":7,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x000003FC : {"name":"unit_status", "id":0x000003FC, "index":0x0C, "size":4,
                  "args": { "unk00":"I", "unit_id":"I", "status":"I", }},
    0x00000401 : {"name":"0x00000401", "id":0x00000401, "index":0x0D, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000406 : {"name":"0x00000406", "id":0x00000406, "index":0x0E, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000040B : {"name":"0x0000040B", "id":0x0000040B, "index":0x0F, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000410 : {"name":"0x00000410", "id":0x00000410, "index":0x10, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000000AA : {"name":"0x000000AA", "id":0x000000AA, "index":0x11, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000041A : {"name":"0x0000041A", "id":0x0000041A, "index":0x12, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000460 : {"name":"0x00000460", "id":0x00000460, "index":0x13, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000004F6 : {"name":"0x000004F6", "id":0x000004F6, "index":0x14, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001F7C : {"name":"0x00001F7C", "id":0x00001F7C, "index":0x15, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x0000006E : {"name":"0x0000006E", "id":0x0000006E, "index":0x16, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x0000008C : {"name":"0x0000008C", "id":0x0000008C, "index":0x17, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000488 : {"name":"0x00000488", "id":0x00000488, "index":0x18, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000048D : {"name":"0x0000048D", "id":0x0000048D, "index":0x19, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000004CE : {"name":"0x000004CE", "id":0x000004CE, "index":0x1A, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000500 : {"name":"0x00000500", "id":0x00000500, "index":0x1B, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000003F3 : {"name":"0x000003F3", "id":0x000003F3, "index":0x1C, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000407 : {"name":"0x00000407", "id":0x00000407, "index":0x1D, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000046A : {"name":"0x0000046A", "id":0x0000046A, "index":0x1E, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000474 : {"name":"0x00000474", "id":0x00000474, "index":0x1F, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00001F90 : {"name":"0x00001F90", "id":0x00001F90, "index":0x20, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000004E2 : {"name":"0x000004E2", "id":0x000004E2, "index":0x21, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x0000050A : {"name":"0x0000050A", "id":0x0000050A, "index":0x22, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000051E : {"name":"0x0000051E", "id":0x0000051E, "index":0x23, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000514 : {"name":"0x00000514", "id":0x00000514, "index":0x24, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x0000042E : {"name":"0x0000042E", "id":0x0000042E, "index":0x25, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x0000049C : {"name":"0x0000049C", "id":0x0000049C, "index":0x26, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000004B0 : {"name":"0x000004B0", "id":0x000004B0, "index":0x27, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000004B5 : {"name":"0x000004B5", "id":0x000004B5, "index":0x28, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000442 : {"name":"0x00000442", "id":0x00000442, "index":0x29, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000004A6 : {"name":"0x000004A6", "id":0x000004A6, "index":0x2A, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000004AB : {"name":"0x000004AB", "id":0x000004AB, "index":0x2B, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000492 : {"name":"0x00000492", "id":0x00000492, "index":0x2C, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000004BA : {"name":"0x000004BA", "id":0x000004BA, "index":0x2D, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000004BF : {"name":"0x000004BF", "id":0x000004BF, "index":0x2E, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000004C4 : {"name":"0x000004C4", "id":0x000004C4, "index":0x2F, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000004D8 : {"name":"0x000004D8", "id":0x000004D8, "index":0x30, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000004EC : {"name":"0x000004EC", "id":0x000004EC, "index":0x31, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000007D0 : {"name":"0x000007D0", "id":0x000007D0, "index":0x32, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001F86 : {"name":"0x00001F86", "id":0x00001F86, "index":0x33, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000007EE : {"name":"0x000007EE", "id":0x000007EE, "index":0x34, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000007F3 : {"name":"0x000007F3", "id":0x000007F3, "index":0x35, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000007F8 : {"name":"0x000007F8", "id":0x000007F8, "index":0x36, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000007EF : {"name":"0x000007EF", "id":0x000007EF, "index":0x37, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000032 : {"name":"0x00000032", "id":0x00000032, "index":0x38, "size":6,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000FA0 : {"name":"0x00000FA0", "id":0x00000FA0, "index":0x39, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000003C : {"name":"0x0000003C", "id":0x0000003C, "index":0x3A, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000041 : {"name":"0x00000041", "id":0x00000041, "index":0x3B, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x0000005A : {"name":"0x0000005A", "id":0x0000005A, "index":0x3C, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000FAA : {"name":"0x00000FAA", "id":0x00000FAA, "index":0x3D, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000000A0 : {"name":"0x000000A0", "id":0x000000A0, "index":0x3E, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FB4 : {"name":"0x00000FB4", "id":0x00000FB4, "index":0x3F, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000FA1 : {"name":"0x00000FA1", "id":0x00000FA1, "index":0x40, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000FBE : {"name":"0x00000FBE", "id":0x00000FBE, "index":0x41, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000BB8 : {"name":"0x00000BB8", "id":0x00000BB8, "index":0x42, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000096 : {"name":"0x00000096", "id":0x00000096, "index":0x43, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001F45 : {"name":"0x00001F45", "id":0x00001F45, "index":0x44, "size":2,
                  "args": { "unk00":"I", }},
    0x00001FC2 : {"name":"0x00001FC2", "id":0x00001FC2, "index":0x45, "size":2,
                  "args": { "unk00":"I", }},
    0x00001F4A : {"name":"0x00001F4A", "id":0x00001F4A, "index":0x46, "size":2,
                  "args": { "unk00":"I", }},
    0x00001F4F : {"name":"0x00001F4F", "id":0x00001F4F, "index":0x47, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00001FB8 : {"name":"0x00001FB8", "id":0x00001FB8, "index":0x48, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001F54 : {"name":"0x00001F54", "id":0x00001F54, "index":0x49, "size":2,
                  "args": { "unk00":"I", }},
    0x00001F5E : {"name":"0x00001F5E", "id":0x00001F5E, "index":0x4A, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001FE0 : {"name":"0x00001FE0", "id":0x00001FE0, "index":0x4B, "size":2,
                  "args": { "unk00":"I", }},
    0x00001F59 : {"name":"0x00001F59", "id":0x00001F59, "index":0x4C, "size":2,
                  "args": { "unk00":"I", }},
    0x00001F63 : {"name":"0x00001F63", "id":0x00001F63, "index":0x4D, "size":2,
                  "args": { "unk00":"I", }},
    0x00001F9A : {"name":"0x00001F9A", "id":0x00001F9A, "index":0x4E, "size":2,
                  "args": { "unk00":"I", }},
    0x00001F68 : {"name":"0x00001F68", "id":0x00001F68, "index":0x4F, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001F72 : {"name":"0x00001F72", "id":0x00001F72, "index":0x50, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001FA4 : {"name":"0x00001FA4", "id":0x00001FA4, "index":0x51, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00001FAE : {"name":"0x00001FAE", "id":0x00001FAE, "index":0x52, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001FCC : {"name":"0x00001FCC", "id":0x00001FCC, "index":0x53, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001FD6 : {"name":"0x00001FD6", "id":0x00001FD6, "index":0x54, "size":2,
                  "args": { "unk00":"I", }},
    0x00000046 : {"name":"0x00000046", "id":0x00000046, "index":0x55, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000028 : {"name":"0x00000028", "id":0x00000028, "index":0x56, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000050 : {"name":"0x00000050", "id":0x00000050, "index":0x57, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000055 : {"name":"0x00000055", "id":0x00000055, "index":0x58, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000424 : {"name":"0x00000424", "id":0x00000424, "index":0x59, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000047E : {"name":"0x0000047E", "id":0x0000047E, "index":0x5A, "size":5,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000000B4 : {"name":"0x000000B4", "id":0x000000B4, "index":0x5B, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000078 : {"name":"0x00000078", "id":0x00000078, "index":0x5C, "size":2,
                  "args": { "unk00":"I", }},
    0x00002328 : {"name":"0x00002328", "id":0x00002328, "index":0x5D, "size":4,
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00002332 : {"name":"0x00002332", "id":0x00002332, "index":0x5E, "size":3,
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000233C : {"name":"0x0000233C", "id":0x0000233C, "index":0x5F, "size":2,
                  "args": { "unk00":"I", }},
    0x00002346 : {"name":"0x00002346", "id":0x00002346, "index":0x60, "size":2,
                  "args": { "unk00":"I", }},
    0x0001869E : {"name":"and", "id":0x0001869E, "index":0x61, "size":4,
                  "args": { "unk00":"I", "num_args":"I", "num_dwords":"I", }},
    0x0001869F : {"name":"or", "id":0x0001869F, "index":0x62, "size":4,
                  "args": { "unk00":"I", "num_args":"i", "num_dwords":"I", }},
    0x00001F40 : {"name":"0x00001F40", "id":0x00001F40, "index":0x63, "size":1,
                  "args": { }},
}

OPCODES_CONDITIONS |= {v["name"]:v for name,v in OPCODES_CONDITIONS.items()}

class script_status:
    args = OPCODES_CONDITIONS[0x00000000]["args"]

    statuses = {
        0: "Complete",
        1: "Incomplete",
    }
    statuses |= {n:v for v,n in statuses.items()}

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_status.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "status":
                out_arg = script_status.statuses[arg]
            elif arg_name == "script_id":
                out_arg = arg
            else:
                print(f"Bad number of args in script_status!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_status.args[name]
            if name == "status":
                out_arg = script_status.statuses[arg]
            elif name == "script_id":
                out_arg = arg
            else:
                print(f"Bad number of args in script_status!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000000A:
    args = OPCODES_CONDITIONS[0x0000000A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000000A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000000A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000000A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000000A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000000B:
    args = OPCODES_CONDITIONS[0x0000000B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000000B.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000000B!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000000B.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000000B!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000014:
    args = OPCODES_CONDITIONS[0x00000014]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000014.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000014!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000014.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000014!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000015:
    args = OPCODES_CONDITIONS[0x00000015]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000015.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000015!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000015.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000015!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000001E:
    args = OPCODES_CONDITIONS[0x0000001E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000001E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000001E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000001E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000001E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000028:
    args = OPCODES_CONDITIONS[0x00000028]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000028.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000028!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000028.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000028!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000032:
    args = OPCODES_CONDITIONS[0x00000032]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000032.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000032!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000032.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000032!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000003C:
    args = OPCODES_CONDITIONS[0x0000003C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000003C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000003C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000003C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000003C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000041:
    args = OPCODES_CONDITIONS[0x00000041]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000041.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000041!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000041.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000041!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000046:
    args = OPCODES_CONDITIONS[0x00000046]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000046.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000046!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000046.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000046!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000050:
    args = OPCODES_CONDITIONS[0x00000050]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000050.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000050!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000050.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000050!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000055:
    args = OPCODES_CONDITIONS[0x00000055]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000055.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000055!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000055.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000055!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000005A:
    args = OPCODES_CONDITIONS[0x0000005A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000005A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000005A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000005A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000005A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000006E:
    args = OPCODES_CONDITIONS[0x0000006E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000006E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000006E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000006E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000006E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000078:
    args = OPCODES_CONDITIONS[0x00000078]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000078.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000078!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000078.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000078!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000082:
    args = OPCODES_CONDITIONS[0x00000082]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000082.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000082!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000082.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000082!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000008C:
    args = OPCODES_CONDITIONS[0x0000008C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000008C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000008C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000008C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000008C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000096:
    args = OPCODES_CONDITIONS[0x00000096]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000096.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000096!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000096.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000096!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000000A0:
    args = OPCODES_CONDITIONS[0x000000A0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000000A0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000000A0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000000A0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000000A0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000000AA:
    args = OPCODES_CONDITIONS[0x000000AA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000000AA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000000AA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000000AA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000000AA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000000B4:
    args = OPCODES_CONDITIONS[0x000000B4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000000B4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000000B4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000000B4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000000B4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000003E8:
    args = OPCODES_CONDITIONS[0x000003E8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000003E8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000003E8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000003E8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000003E8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000003F2:
    args = OPCODES_CONDITIONS[0x000003F2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000003F2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000003F2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000003F2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000003F2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000003F3:
    args = OPCODES_CONDITIONS[0x000003F3]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000003F3.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000003F3!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000003F3.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000003F3!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000003F7:
    args = OPCODES_CONDITIONS[0x000003F7]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000003F7.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk14":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000003F7!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000003F7.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            elif name == "unk14":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000003F7!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000003FA:
    args = OPCODES_CONDITIONS[0x000003FA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000003FA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk14":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk18":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000003FA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000003FA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            elif name == "unk14":
                out_arg = int(arg, 0)
            elif name == "unk18":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000003FA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class unit_status:
    args = OPCODES_CONDITIONS[0x000003FC]["args"]

    statuses = {
        0: "Alive",
        2: "Defeated",
    }
    statuses |= {n:v for v,n in statuses.items()}

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(unit_status.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unit_id":
                if arg in unit_defs:
                    out_arg = f"0x{arg:X} ({unit_defs[arg]})"
                else:
                    out_arg = f"0x{arg:X} ()"
            elif arg_name == "status":
                out_arg = unit_status.statuses[arg]
            else:
                print(f"Bad number of args in unit_status!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = unit_status.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "status":
                out_arg = unit_status.statuses[arg]
            else:
                print(f"Bad number of args in unit_status!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000401:
    args = OPCODES_CONDITIONS[0x00000401]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000401.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000401!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000401.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000401!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000406:
    args = OPCODES_CONDITIONS[0x00000406]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000406.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000406!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000406.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000406!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000407:
    args = OPCODES_CONDITIONS[0x00000407]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000407.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000407!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000407.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000407!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000040B:
    args = OPCODES_CONDITIONS[0x0000040B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000040B.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000040B!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000040B.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000040B!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000410:
    args = OPCODES_CONDITIONS[0x00000410]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000410.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000410!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000410.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000410!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000041A:
    args = OPCODES_CONDITIONS[0x0000041A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000041A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000041A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000041A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000041A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000424:
    args = OPCODES_CONDITIONS[0x00000424]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000424.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000424!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000424.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000424!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000042E:
    args = OPCODES_CONDITIONS[0x0000042E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000042E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000042E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000042E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000042E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000442:
    args = OPCODES_CONDITIONS[0x00000442]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000442.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000442!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000442.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000442!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000460:
    args = OPCODES_CONDITIONS[0x00000460]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000460.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000460!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000460.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000460!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000046A:
    args = OPCODES_CONDITIONS[0x0000046A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000046A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000046A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000046A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000046A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000474:
    args = OPCODES_CONDITIONS[0x00000474]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000474.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000474!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000474.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000474!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000047E:
    args = OPCODES_CONDITIONS[0x0000047E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000047E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000047E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000047E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000047E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000488:
    args = OPCODES_CONDITIONS[0x00000488]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000488.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000488!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000488.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000488!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000048D:
    args = OPCODES_CONDITIONS[0x0000048D]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000048D.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000048D!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000048D.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000048D!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000492:
    args = OPCODES_CONDITIONS[0x00000492]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000492.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000492!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000492.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000492!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000049C:
    args = OPCODES_CONDITIONS[0x0000049C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000049C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000049C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000049C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000049C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004A6:
    args = OPCODES_CONDITIONS[0x000004A6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004A6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004A6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004A6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004A6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004AB:
    args = OPCODES_CONDITIONS[0x000004AB]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004AB.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004AB!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004AB.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004AB!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004B0:
    args = OPCODES_CONDITIONS[0x000004B0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004B0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004B0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004B0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004B0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004B5:
    args = OPCODES_CONDITIONS[0x000004B5]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004B5.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004B5!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004B5.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004B5!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004BA:
    args = OPCODES_CONDITIONS[0x000004BA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004BA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004BA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004BA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004BA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004BF:
    args = OPCODES_CONDITIONS[0x000004BF]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004BF.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004BF!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004BF.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004BF!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004C4:
    args = OPCODES_CONDITIONS[0x000004C4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004C4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004C4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004C4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004C4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004CE:
    args = OPCODES_CONDITIONS[0x000004CE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004CE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004CE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004CE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004CE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004D8:
    args = OPCODES_CONDITIONS[0x000004D8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004D8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004D8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004D8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004D8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004E2:
    args = OPCODES_CONDITIONS[0x000004E2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004E2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004E2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004E2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004E2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004EC:
    args = OPCODES_CONDITIONS[0x000004EC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004EC.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004EC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004EC.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004EC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000004F6:
    args = OPCODES_CONDITIONS[0x000004F6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000004F6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000004F6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000004F6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000004F6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000500:
    args = OPCODES_CONDITIONS[0x00000500]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000500.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000500!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000500.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000500!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000050A:
    args = OPCODES_CONDITIONS[0x0000050A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000050A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000050A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000050A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000050A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000514:
    args = OPCODES_CONDITIONS[0x00000514]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000514.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000514!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000514.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000514!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000051E:
    args = OPCODES_CONDITIONS[0x0000051E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000051E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000051E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000051E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000051E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000528:
    args = OPCODES_CONDITIONS[0x00000528]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000528.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk14":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000528!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000528.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            elif name == "unk14":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000528!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000007D0:
    args = OPCODES_CONDITIONS[0x000007D0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000007D0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000007D0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000007D0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000007D0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000007EE:
    args = OPCODES_CONDITIONS[0x000007EE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000007EE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000007EE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000007EE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000007EE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000007EF:
    args = OPCODES_CONDITIONS[0x000007EF]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000007EF.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000007EF!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000007EF.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000007EF!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000007F3:
    args = OPCODES_CONDITIONS[0x000007F3]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000007F3.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000007F3!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000007F3.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000007F3!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_000007F8:
    args = OPCODES_CONDITIONS[0x000007F8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_000007F8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_000007F8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_000007F8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_000007F8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000BB8:
    args = OPCODES_CONDITIONS[0x00000BB8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000BB8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000BB8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000BB8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000BB8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000FA0:
    args = OPCODES_CONDITIONS[0x00000FA0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000FA0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000FA0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000FA0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000FA0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000FA1:
    args = OPCODES_CONDITIONS[0x00000FA1]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000FA1.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000FA1!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000FA1.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000FA1!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000FAA:
    args = OPCODES_CONDITIONS[0x00000FAA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000FAA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000FAA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000FAA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000FAA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000FB4:
    args = OPCODES_CONDITIONS[0x00000FB4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000FB4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000FB4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000FB4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000FB4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00000FBE:
    args = OPCODES_CONDITIONS[0x00000FBE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00000FBE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00000FBE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00000FBE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00000FBE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F40:
    args = OPCODES_CONDITIONS[0x00001F40]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class condition_00001F45:
    args = OPCODES_CONDITIONS[0x00001F45]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F45.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F45!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F45.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F45!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F4A:
    args = OPCODES_CONDITIONS[0x00001F4A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F4A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F4A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F4A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F4A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F4F:
    args = OPCODES_CONDITIONS[0x00001F4F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F4F.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F4F!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F4F.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F4F!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F54:
    args = OPCODES_CONDITIONS[0x00001F54]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F54.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F54!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F54.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F54!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F59:
    args = OPCODES_CONDITIONS[0x00001F59]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F59.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F59!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F59.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F59!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F5E:
    args = OPCODES_CONDITIONS[0x00001F5E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F5E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F5E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F5E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F5E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F63:
    args = OPCODES_CONDITIONS[0x00001F63]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F63.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F63!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F63.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F63!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F68:
    args = OPCODES_CONDITIONS[0x00001F68]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F68.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F68!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F68.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F68!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F72:
    args = OPCODES_CONDITIONS[0x00001F72]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F72.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F72!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F72.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F72!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F7C:
    args = OPCODES_CONDITIONS[0x00001F7C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F7C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F7C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F7C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F7C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F86:
    args = OPCODES_CONDITIONS[0x00001F86]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F86.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F86!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F86.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F86!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F90:
    args = OPCODES_CONDITIONS[0x00001F90]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F90.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk10":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F90!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F90.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            elif name == "unk10":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F90!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001F9A:
    args = OPCODES_CONDITIONS[0x00001F9A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001F9A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001F9A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001F9A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001F9A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001FA4:
    args = OPCODES_CONDITIONS[0x00001FA4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001FA4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001FA4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001FA4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001FA4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001FAE:
    args = OPCODES_CONDITIONS[0x00001FAE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001FAE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001FAE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001FAE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001FAE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001FB8:
    args = OPCODES_CONDITIONS[0x00001FB8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001FB8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001FB8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001FB8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001FB8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001FC2:
    args = OPCODES_CONDITIONS[0x00001FC2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001FC2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001FC2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001FC2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001FC2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001FCC:
    args = OPCODES_CONDITIONS[0x00001FCC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001FCC.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001FCC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001FCC.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001FCC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001FD6:
    args = OPCODES_CONDITIONS[0x00001FD6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001FD6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001FD6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001FD6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001FD6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00001FE0:
    args = OPCODES_CONDITIONS[0x00001FE0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00001FE0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00001FE0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00001FE0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00001FE0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00002328:
    args = OPCODES_CONDITIONS[0x00002328]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00002328.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00002328!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00002328.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00002328!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00002332:
    args = OPCODES_CONDITIONS[0x00002332]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00002332.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00002332!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00002332.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00002332!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_0000233C:
    args = OPCODES_CONDITIONS[0x0000233C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_0000233C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_0000233C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_0000233C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_0000233C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_00002346:
    args = OPCODES_CONDITIONS[0x00002346]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_00002346.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_00002346!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_00002346.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in condition_00002346!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_and:
    args = OPCODES_CONDITIONS[0x0001869E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_and.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "num_args":
                out_arg = arg
            elif arg_name == "num_dwords":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_and!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        def get_num_args(op):
            v = 0
            for o in op:
                v += OPCODES_CONDITIONS[o["opcode"]]["size"]
                if "opcodes" in o:
                    v += get_num_args(o["opcodes"])
            return v

        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_and.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "num_args":
                if "opcodes" in opcode:
                    out_arg = len(opcode["opcodes"])
                else:
                    out_arg = 0
            elif name == "num_dwords":
                out_arg = 0
                if "opcodes" in opcode:
                    out_arg = get_num_args(opcode["opcodes"])
            else:
                print(f"Bad number of args in condition_and!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class condition_or:
    args = OPCODES_CONDITIONS[0x0001869F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(condition_or.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "num_args":
                out_arg = arg
            elif arg_name == "num_dwords":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in condition_or!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        def get_num_args(op):
            v = 0
            for o in op:
                v += OPCODES_CONDITIONS[o["opcode"]]["size"]
                if "opcodes" in o:
                    v += get_num_args(o["opcodes"])
            return v
            
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = condition_or.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "num_args":
                if "opcodes" in opcode:
                    out_arg = len(opcode["opcodes"])
                else:
                    out_arg = 0
            elif name == "num_dwords":
                out_arg = 0
                if "opcodes" in opcode:
                    out_arg = get_num_args(opcode["opcodes"])
            else:
                print(f"Bad number of args in condition_or!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        


HANDLERS_CONDITIONS = {
    0x00000000:script_status,
    0x0000000A:condition_0000000A,
    0x0000000B:condition_0000000B,
    0x00000014:condition_00000014,
    0x00000015:condition_00000015,
    0x0000001E:condition_0000001E,
    0x00000028:condition_00000028,
    0x00000032:condition_00000032,
    0x0000003C:condition_0000003C,
    0x00000041:condition_00000041,
    0x00000046:condition_00000046,
    0x00000050:condition_00000050,
    0x00000055:condition_00000055,
    0x0000005A:condition_0000005A,
    0x0000006E:condition_0000006E,
    0x00000078:condition_00000078,
    0x00000082:condition_00000082,
    0x0000008C:condition_0000008C,
    0x00000096:condition_00000096,
    0x000000A0:condition_000000A0,
    0x000000AA:condition_000000AA,
    0x000000B4:condition_000000B4,
    0x000003E8:condition_000003E8,
    0x000003F2:condition_000003F2,
    0x000003F3:condition_000003F3,
    0x000003F7:condition_000003F7,
    0x000003FA:condition_000003FA,
    0x000003FC:unit_status,
    0x00000401:condition_00000401,
    0x00000406:condition_00000406,
    0x00000407:condition_00000407,
    0x0000040B:condition_0000040B,
    0x00000410:condition_00000410,
    0x0000041A:condition_0000041A,
    0x00000424:condition_00000424,
    0x0000042E:condition_0000042E,
    0x00000442:condition_00000442,
    0x00000460:condition_00000460,
    0x0000046A:condition_0000046A,
    0x00000474:condition_00000474,
    0x0000047E:condition_0000047E,
    0x00000488:condition_00000488,
    0x0000048D:condition_0000048D,
    0x00000492:condition_00000492,
    0x0000049C:condition_0000049C,
    0x000004A6:condition_000004A6,
    0x000004AB:condition_000004AB,
    0x000004B0:condition_000004B0,
    0x000004B5:condition_000004B5,
    0x000004BA:condition_000004BA,
    0x000004BF:condition_000004BF,
    0x000004C4:condition_000004C4,
    0x000004CE:condition_000004CE,
    0x000004D8:condition_000004D8,
    0x000004E2:condition_000004E2,
    0x000004EC:condition_000004EC,
    0x000004F6:condition_000004F6,
    0x00000500:condition_00000500,
    0x0000050A:condition_0000050A,
    0x00000514:condition_00000514,
    0x0000051E:condition_0000051E,
    0x00000528:condition_00000528,
    0x000007D0:condition_000007D0,
    0x000007EE:condition_000007EE,
    0x000007EF:condition_000007EF,
    0x000007F3:condition_000007F3,
    0x000007F8:condition_000007F8,
    0x00000BB8:condition_00000BB8,
    0x00000FA0:condition_00000FA0,
    0x00000FA1:condition_00000FA1,
    0x00000FAA:condition_00000FAA,
    0x00000FB4:condition_00000FB4,
    0x00000FBE:condition_00000FBE,
    0x00001F40:condition_00001F40,
    0x00001F45:condition_00001F45,
    0x00001F4A:condition_00001F4A,
    0x00001F4F:condition_00001F4F,
    0x00001F54:condition_00001F54,
    0x00001F59:condition_00001F59,
    0x00001F5E:condition_00001F5E,
    0x00001F63:condition_00001F63,
    0x00001F68:condition_00001F68,
    0x00001F72:condition_00001F72,
    0x00001F7C:condition_00001F7C,
    0x00001F86:condition_00001F86,
    0x00001F90:condition_00001F90,
    0x00001F9A:condition_00001F9A,
    0x00001FA4:condition_00001FA4,
    0x00001FAE:condition_00001FAE,
    0x00001FB8:condition_00001FB8,
    0x00001FC2:condition_00001FC2,
    0x00001FCC:condition_00001FCC,
    0x00001FD6:condition_00001FD6,
    0x00001FE0:condition_00001FE0,
    0x00002328:condition_00002328,
    0x00002332:condition_00002332,
    0x0000233C:condition_0000233C,
    0x00002346:condition_00002346,
    0x0001869E:condition_and,
    0x0001869F:condition_or,
}
