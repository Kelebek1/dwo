import struct
import chars
import read_string_file

OPCODES_SCRIPT = {
    0x00000000 : {"name":"show_notification", "id":0x00000000, "index":0x00, "size":11, 
                  "args": { "msg_id":"I", "s0":"I", "s1":"I", "s2":"I", "s3":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", }},
    0x0000000A : {"name":"play_speech", "id":0x0000000A, "index":0x01, "size":5, 
                  "args": { "msg_id":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000014 : {"name":"0x00000014", "id":0x00000014, "index":0x02, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000001E : {"name":"0x0000001E", "id":0x0000001E, "index":0x03, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000032 : {"name":"0x00000032", "id":0x00000032, "index":0x04, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000003C : {"name":"0x0000003C", "id":0x0000003C, "index":0x05, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000046 : {"name":"0x00000046", "id":0x00000046, "index":0x06, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000028 : {"name":"0x00000028", "id":0x00000028, "index":0x07, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001F68 : {"name":"0x00001F68", "id":0x00001F68, "index":0x08, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000050 : {"name":"0x00000050", "id":0x00000050, "index":0x09, "size":10, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", }},
    0x0000005A : {"name":"0x0000005A", "id":0x0000005A, "index":0x0A, "size":1, 
                  "args": { }},
    0x00000064 : {"name":"0x00000064", "id":0x00000064, "index":0x0B, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000003E8 : {"name":"unit_ping", "id":0x000003E8, "index":0x0C, "size":3, 
                  "args": { "unit_id":"I", "unk04":"I", }},
    0x000003ED : {"name":"0x000003ED", "id":0x000003ED, "index":0x0D, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000003EF : {"name":"0x000003EF", "id":0x000003EF, "index":0x0E, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000003F2 : {"name":"0x000003F2", "id":0x000003F2, "index":0x0F, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000003FC : {"name":"0x000003FC", "id":0x000003FC, "index":0x10, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000406 : {"name":"0x00000406", "id":0x00000406, "index":0x11, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000410 : {"name":"0x00000410", "id":0x00000410, "index":0x12, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000041A : {"name":"0x0000041A", "id":0x0000041A, "index":0x13, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000424 : {"name":"0x00000424", "id":0x00000424, "index":0x14, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000042E : {"name":"0x0000042E", "id":0x0000042E, "index":0x15, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x00000438 : {"name":"0x00000438", "id":0x00000438, "index":0x16, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000442 : {"name":"0x00000442", "id":0x00000442, "index":0x17, "size":10, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", }},
    0x0000044C : {"name":"0x0000044C", "id":0x0000044C, "index":0x18, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000456 : {"name":"0x00000456", "id":0x00000456, "index":0x19, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000045B : {"name":"0x0000045B", "id":0x0000045B, "index":0x1A, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000460 : {"name":"0x00000460", "id":0x00000460, "index":0x1B, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000465 : {"name":"0x00000465", "id":0x00000465, "index":0x1C, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000046A : {"name":"0x0000046A", "id":0x0000046A, "index":0x1D, "size":9, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", }},
    0x00000474 : {"name":"0x00000474", "id":0x00000474, "index":0x1E, "size":10, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", }},
    0x00000479 : {"name":"0x00000479", "id":0x00000479, "index":0x1F, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x0000047E : {"name":"0x0000047E", "id":0x0000047E, "index":0x20, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000007D0 : {"name":"0x000007D0", "id":0x000007D0, "index":0x21, "size":2, 
                  "args": { "unk00":"I", }},
    0x000007DA : {"name":"0x000007DA", "id":0x000007DA, "index":0x22, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x000007E4 : {"name":"0x000007E4", "id":0x000007E4, "index":0x23, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000007EE : {"name":"0x000007EE", "id":0x000007EE, "index":0x24, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000007F8 : {"name":"0x000007F8", "id":0x000007F8, "index":0x25, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000802 : {"name":"0x00000802", "id":0x00000802, "index":0x26, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001004 : {"name":"0x00001004", "id":0x00001004, "index":0x27, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001068 : {"name":"0x00001068", "id":0x00001068, "index":0x28, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000BB8 : {"name":"unit_set_active", "id":0x00000BB8, "index":0x29, "size":3, 
                  "args": { "unit_id":"I", "unk04":"I", }},
    0x00000BC2 : {"name":"0x00000BC2", "id":0x00000BC2, "index":0x2A, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000BC7 : {"name":"0x00000BC7", "id":0x00000BC7, "index":0x2B, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000BD6 : {"name":"0x00000BD6", "id":0x00000BD6, "index":0x2C, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000BE0 : {"name":"0x00000BE0", "id":0x00000BE0, "index":0x2D, "size":4, 
                  "args": { "unit_id":"I", "unk04":"I", "unk08":"I", }},
    0x00000BE5 : {"name":"0x00000BE5", "id":0x00000BE5, "index":0x2E, "size":8, 
                  "args": { "unit_id":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", }},
    0x00000BEA : {"name":"0x00000BEA", "id":0x00000BEA, "index":0x2F, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000BF4 : {"name":"unit_kill", "id":0x00000BF4, "index":0x30, "size":2, 
                  "args": { "unit_id":"I", }},
    0x00000BFE : {"name":"0x00000BFE", "id":0x00000BFE, "index":0x31, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000C03 : {"name":"0x00000C03", "id":0x00000C03, "index":0x32, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x00000E01 : {"name":"0x00000E01", "id":0x00000E01, "index":0x33, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000E10 : {"name":"0x00000E10", "id":0x00000E10, "index":0x34, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000DFC : {"name":"0x00000DFC", "id":0x00000DFC, "index":0x35, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000CEE : {"name":"unit_change_name", "id":0x00000CEE, "index":0x36, "size":3, 
                  "args": { "unit_id":"I", "name":"I", }},
    0x00000C08 : {"name":"0x00000C08", "id":0x00000C08, "index":0x37, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000DF2 : {"name":"0x00000DF2", "id":0x00000DF2, "index":0x38, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000C0D : {"name":"0x00000C0D", "id":0x00000C0D, "index":0x39, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000C12 : {"name":"0x00000C12", "id":0x00000C12, "index":0x3A, "size":9, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", }},
    0x00000C30 : {"name":"0x00000C30", "id":0x00000C30, "index":0x3B, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000C44 : {"name":"unit_set_courage", "id":0x00000C44, "index":0x3C, "size":5, 
                  "args": { "unit_id":"I", "level":"i", "unk08":"I", "unk0C":"I", }},
    0x00000C58 : {"name":"0x00000C58", "id":0x00000C58, "index":0x3D, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000CE4 : {"name":"0x00000CE4", "id":0x00000CE4, "index":0x3E, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000CE9 : {"name":"0x00000CE9", "id":0x00000CE9, "index":0x3F, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000C85 : {"name":"0x00000C85", "id":0x00000C85, "index":0x40, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000C8A : {"name":"change_morale", "id":0x00000C8A, "index":0x41, "size":5, 
                  "args": { "force":"I", "dir":"I", "amount":"i", "unk0C":"I", }},
    0x00000C9E : {"name":"0x00000C9E", "id":0x00000C9E, "index":0x42, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D0C : {"name":"0x00000D0C", "id":0x00000D0C, "index":0x43, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D16 : {"name":"0x00000D16", "id":0x00000D16, "index":0x44, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000D20 : {"name":"0x00000D20", "id":0x00000D20, "index":0x45, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000D25 : {"name":"0x00000D25", "id":0x00000D25, "index":0x46, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000C4E : {"name":"0x00000C4E", "id":0x00000C4E, "index":0x47, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000CA8 : {"name":"0x00000CA8", "id":0x00000CA8, "index":0x48, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000CB2 : {"name":"0x00000CB2", "id":0x00000CB2, "index":0x49, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000CBC : {"name":"0x00000CBC", "id":0x00000CBC, "index":0x4A, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x00000CC6 : {"name":"0x00000CC6", "id":0x00000CC6, "index":0x4B, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000CD0 : {"name":"0x00000CD0", "id":0x00000CD0, "index":0x4C, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000CDA : {"name":"0x00000CDA", "id":0x00000CDA, "index":0x4D, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001FD6 : {"name":"0x00001FD6", "id":0x00001FD6, "index":0x4E, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000CF8 : {"name":"0x00000CF8", "id":0x00000CF8, "index":0x4F, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D66 : {"name":"0x00000D66", "id":0x00000D66, "index":0x50, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D6B : {"name":"0x00000D6B", "id":0x00000D6B, "index":0x51, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D2A : {"name":"0x00000D2A", "id":0x00000D2A, "index":0x52, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000D34 : {"name":"0x00000D34", "id":0x00000D34, "index":0x53, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000D52 : {"name":"0x00000D52", "id":0x00000D52, "index":0x54, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000E06 : {"name":"0x00000E06", "id":0x00000E06, "index":0x55, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000D8E : {"name":"0x00000D8E", "id":0x00000D8E, "index":0x56, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000DAC : {"name":"0x00000DAC", "id":0x00000DAC, "index":0x57, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000DD4 : {"name":"0x00000DD4", "id":0x00000DD4, "index":0x58, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000DDE : {"name":"0x00000DDE", "id":0x00000DDE, "index":0x59, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000DE8 : {"name":"0x00000DE8", "id":0x00000DE8, "index":0x5A, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000E0B : {"name":"0x00000E0B", "id":0x00000E0B, "index":0x5B, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000C21 : {"name":"0x00000C21", "id":0x00000C21, "index":0x5C, "size":8, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", }},
    0x00000C2B : {"name":"unit_move", "id":0x00000C2B, "index":0x5D, "size":12, 
                  "args": { "unit_id":"I", "unk04":"I", "unk08":"I", "target":"I", "x":"I", "y":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", "unk28":"I", }},
    0x00000C3F : {"name":"0x00000C3F", "id":0x00000C3F, "index":0x5E, "size":8, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", }},
    0x00000C35 : {"name":"0x00000C35", "id":0x00000C35, "index":0x5F, "size":12, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", "unk28":"I", }},
    0x00000C3A : {"name":"0x00000C3A", "id":0x00000C3A, "index":0x60, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x00000D70 : {"name":"0x00000D70", "id":0x00000D70, "index":0x61, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000C93 : {"name":"0x00000C93", "id":0x00000C93, "index":0x62, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000D84 : {"name":"0x00000D84", "id":0x00000D84, "index":0x63, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000C49 : {"name":"0x00000C49", "id":0x00000C49, "index":0x64, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D02 : {"name":"0x00000D02", "id":0x00000D02, "index":0x65, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000D07 : {"name":"0x00000D07", "id":0x00000D07, "index":0x66, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000C94 : {"name":"0x00000C94", "id":0x00000C94, "index":0x67, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00002012 : {"name":"0x00002012", "id":0x00002012, "index":0x68, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x00000D48 : {"name":"0x00000D48", "id":0x00000D48, "index":0x69, "size":9, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", }},
    0x00000D7A : {"name":"0x00000D7A", "id":0x00000D7A, "index":0x6A, "size":9, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", }},
    0x00000D7B : {"name":"0x00000D7B", "id":0x00000D7B, "index":0x6B, "size":9, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", }},
    0x00000D9D : {"name":"0x00000D9D", "id":0x00000D9D, "index":0x6C, "size":18, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", "unk28":"I", "unk2C":"I", "unk30":"I", "unk34":"I", "unk38":"I", "unk3C":"I", "unk40":"I", }},
    0x00000D9F : {"name":"0x00000D9F", "id":0x00000D9F, "index":0x6D, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000D98 : {"name":"0x00000D98", "id":0x00000D98, "index":0x6E, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D3E : {"name":"0x00000D3E", "id":0x00000D3E, "index":0x6F, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000D5C : {"name":"0x00000D5C", "id":0x00000D5C, "index":0x70, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000DB6 : {"name":"0x00000DB6", "id":0x00000DB6, "index":0x71, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000DC0 : {"name":"0x00000DC0", "id":0x00000DC0, "index":0x72, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x00000DCA : {"name":"0x00000DCA", "id":0x00000DCA, "index":0x73, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000FA0 : {"name":"0x00000FA0", "id":0x00000FA0, "index":0x74, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000FAA : {"name":"0x00000FAA", "id":0x00000FAA, "index":0x75, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FAF : {"name":"0x00000FAF", "id":0x00000FAF, "index":0x76, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FA5 : {"name":"0x00000FA5", "id":0x00000FA5, "index":0x77, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FAD : {"name":"0x00000FAD", "id":0x00000FAD, "index":0x78, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000FAE : {"name":"0x00000FAE", "id":0x00000FAE, "index":0x79, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FB4 : {"name":"0x00000FB4", "id":0x00000FB4, "index":0x7A, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FB5 : {"name":"0x00000FB5", "id":0x00000FB5, "index":0x7B, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FB7 : {"name":"0x00000FB7", "id":0x00000FB7, "index":0x7C, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FB9 : {"name":"0x00000FB9", "id":0x00000FB9, "index":0x7D, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000100E : {"name":"0x0000100E", "id":0x0000100E, "index":0x7E, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001018 : {"name":"0x00001018", "id":0x00001018, "index":0x7F, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000104A : {"name":"0x0000104A", "id":0x0000104A, "index":0x80, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000104F : {"name":"0x0000104F", "id":0x0000104F, "index":0x81, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000FE6 : {"name":"0x00000FE6", "id":0x00000FE6, "index":0x82, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00000FF0 : {"name":"0x00000FF0", "id":0x00000FF0, "index":0x83, "size":2, 
                  "args": { "unk00":"I", }},
    0x00000FF5 : {"name":"0x00000FF5", "id":0x00000FF5, "index":0x84, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001022 : {"name":"0x00001022", "id":0x00001022, "index":0x85, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001027 : {"name":"0x00001027", "id":0x00001027, "index":0x86, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x0000102C : {"name":"0x0000102C", "id":0x0000102C, "index":0x87, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00000FFA : {"name":"0x00000FFA", "id":0x00000FFA, "index":0x88, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x00000FBE : {"name":"0x00000FBE", "id":0x00000FBE, "index":0x89, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001040 : {"name":"0x00001040", "id":0x00001040, "index":0x8A, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001036 : {"name":"0x00001036", "id":0x00001036, "index":0x8B, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001054 : {"name":"0x00001054", "id":0x00001054, "index":0x8C, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000105E : {"name":"0x0000105E", "id":0x0000105E, "index":0x8D, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001072 : {"name":"0x00001072", "id":0x00001072, "index":0x8E, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000107C : {"name":"0x0000107C", "id":0x0000107C, "index":0x8F, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001770 : {"name":"0x00001770", "id":0x00001770, "index":0x90, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001775 : {"name":"0x00001775", "id":0x00001775, "index":0x91, "size":3, 
                  "args": { "unk00":"I", "unit_id":"I", }},
    0x0000177A : {"name":"0x0000177A", "id":0x0000177A, "index":0x92, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001784 : {"name":"0x00001784", "id":0x00001784, "index":0x93, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000178E : {"name":"0x0000178E", "id":0x0000178E, "index":0x94, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001798 : {"name":"0x00001798", "id":0x00001798, "index":0x95, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000017A2 : {"name":"0x000017A2", "id":0x000017A2, "index":0x96, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000017AC : {"name":"0x000017AC", "id":0x000017AC, "index":0x97, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x0000206C : {"name":"0x0000206C", "id":0x0000206C, "index":0x98, "size":12, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", "unk28":"I", }},
    0x00002076 : {"name":"0x00002076", "id":0x00002076, "index":0x99, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000207B : {"name":"0x0000207B", "id":0x0000207B, "index":0x9A, "size":2, 
                  "args": { "unk00":"I", }},
    0x00002080 : {"name":"0x00002080", "id":0x00002080, "index":0x9B, "size":7, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", }},
    0x0000208A : {"name":"0x0000208A", "id":0x0000208A, "index":0x9C, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x0000208F : {"name":"0x0000208F", "id":0x0000208F, "index":0x9D, "size":2, 
                  "args": { "unk00":"I", }},
    0x00002090 : {"name":"0x00002090", "id":0x00002090, "index":0x9E, "size":11, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", }},
    0x00002094 : {"name":"0x00002094", "id":0x00002094, "index":0x9F, "size":8, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", }},
    0x0000209E : {"name":"0x0000209E", "id":0x0000209E, "index":0xA0, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00001388 : {"name":"0x00001388", "id":0x00001388, "index":0xA1, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001392 : {"name":"0x00001392", "id":0x00001392, "index":0xA2, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x0000139C : {"name":"0x0000139C", "id":0x0000139C, "index":0xA3, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000013A1 : {"name":"0x000013A1", "id":0x000013A1, "index":0xA4, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000013A4 : {"name":"0x000013A4", "id":0x000013A4, "index":0xA5, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x000013A6 : {"name":"0x000013A6", "id":0x000013A6, "index":0xA6, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000013B0 : {"name":"0x000013B0", "id":0x000013B0, "index":0xA7, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000013CE : {"name":"0x000013CE", "id":0x000013CE, "index":0xA8, "size":2, 
                  "args": { "unk00":"I", }},
    0x000013D8 : {"name":"0x000013D8", "id":0x000013D8, "index":0xA9, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x000013BA : {"name":"0x000013BA", "id":0x000013BA, "index":0xAA, "size":6, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", }},
    0x000013C4 : {"name":"0x000013C4", "id":0x000013C4, "index":0xAB, "size":1, 
                  "args": { }},
    0x000013E2 : {"name":"0x000013E2", "id":0x000013E2, "index":0xAC, "size":10, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", }},
    0x000013E5 : {"name":"0x000013E5", "id":0x000013E5, "index":0xAD, "size":10, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", }},
    0x000013E7 : {"name":"0x000013E7", "id":0x000013E7, "index":0xAE, "size":10, 
                  "args": { "unit_id":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", }},
    0x00001450 : {"name":"0x00001450", "id":0x00001450, "index":0xAF, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001432 : {"name":"0x00001432", "id":0x00001432, "index":0xB0, "size":2, 
                  "args": { "unk00":"I", }},
    0x000013EC : {"name":"0x000013EC", "id":0x000013EC, "index":0xB1, "size":11, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", }},
    0x000013F6 : {"name":"0x000013F6", "id":0x000013F6, "index":0xB2, "size":1, 
                  "args": { }},
    0x00001400 : {"name":"0x00001400", "id":0x00001400, "index":0xB3, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001414 : {"name":"0x00001414", "id":0x00001414, "index":0xB4, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000140A : {"name":"0x0000140A", "id":0x0000140A, "index":0xB5, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000140F : {"name":"0x0000140F", "id":0x0000140F, "index":0xB6, "size":1, 
                  "args": { }},
    0x0000143C : {"name":"0x0000143C", "id":0x0000143C, "index":0xB7, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001446 : {"name":"0x00001446", "id":0x00001446, "index":0xB8, "size":1, 
                  "args": { }},
    0x0000141E : {"name":"0x0000141E", "id":0x0000141E, "index":0xB9, "size":11, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", "unk10":"I", "unk14":"I", "unk18":"I", "unk1C":"I", "unk20":"I", "unk24":"I", }},
    0x00001428 : {"name":"0x00001428", "id":0x00001428, "index":0xBA, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001F40 : {"name":"0x00001F40", "id":0x00001F40, "index":0xBB, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001FC2 : {"name":"end_battle", "id":0x00001FC2, "index":0xBC, "size":2, 
                  "args": { "state":"I", }},
    0x00001F4A : {"name":"defeat_condition", "id":0x00001F4A, "index":0xBD, "size":6, 
                  "args": { "string":"I", "s0":"I", "s1":"I", "s2":"I", "s3":"I", }},
    0x00001F54 : {"name":"victory_condition", "id":0x00001F54, "index":0xBE, "size":6, 
                  "args": { "string":"I", "s0":"I", "s1":"I", "s2":"I", "s3":"I", }},
    0x00001FAE : {"name":"0x00001FAE", "id":0x00001FAE, "index":0xBF, "size":1, 
                  "args": { }},
    0x00001FB3 : {"name":"0x00001FB3", "id":0x00001FB3, "index":0xC0, "size":1, 
                  "args": { }},
    0x00001FB8 : {"name":"0x00001FB8", "id":0x00001FB8, "index":0xC1, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000203A : {"name":"0x0000203A", "id":0x0000203A, "index":0xC2, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00002058 : {"name":"0x00002058", "id":0x00002058, "index":0xC3, "size":1, 
                  "args": { }},
    0x00001F90 : {"name":"0x00001F90", "id":0x00001F90, "index":0xC4, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001F9A : {"name":"0x00001F9A", "id":0x00001F9A, "index":0xC5, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00001FA4 : {"name":"0x00001FA4", "id":0x00001FA4, "index":0xC6, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00002026 : {"name":"0x00002026", "id":0x00002026, "index":0xC7, "size":2, 
                  "args": { "unk00":"I", }},
    0x00002030 : {"name":"0x00002030", "id":0x00002030, "index":0xC8, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001F7C : {"name":"0x00001F7C", "id":0x00001F7C, "index":0xC9, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001FE0 : {"name":"0x00001FE0", "id":0x00001FE0, "index":0xCA, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001FEA : {"name":"0x00001FEA", "id":0x00001FEA, "index":0xCB, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001FF4 : {"name":"0x00001FF4", "id":0x00001FF4, "index":0xCC, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00001FFE : {"name":"0x00001FFE", "id":0x00001FFE, "index":0xCD, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00002008 : {"name":"0x00002008", "id":0x00002008, "index":0xCE, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001F86 : {"name":"0x00001F86", "id":0x00001F86, "index":0xCF, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00002044 : {"name":"0x00002044", "id":0x00002044, "index":0xD0, "size":2, 
                  "args": { "unk00":"I", }},
    0x00001FCC : {"name":"0x00001FCC", "id":0x00001FCC, "index":0xD1, "size":2, 
                  "args": { "unk00":"I", }},
    0x00002062 : {"name":"0x00002062", "id":0x00002062, "index":0xD2, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000201C : {"name":"0x0000201C", "id":0x0000201C, "index":0xD3, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000204E : {"name":"0x0000204E", "id":0x0000204E, "index":0xD4, "size":1, 
                  "args": { }},
    0x00002328 : {"name":"0x00002328", "id":0x00002328, "index":0xD5, "size":1, 
                  "args": { }},
    0x00002332 : {"name":"0x00002332", "id":0x00002332, "index":0xD6, "size":1, 
                  "args": { }},
    0x0000233C : {"name":"0x0000233C", "id":0x0000233C, "index":0xD7, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00002341 : {"name":"0x00002341", "id":0x00002341, "index":0xD8, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00002346 : {"name":"0x00002346", "id":0x00002346, "index":0xD9, "size":5, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", "unk0C":"I", }},
    0x00000DA2 : {"name":"0x00000DA2", "id":0x00000DA2, "index":0xDA, "size":4, 
                  "args": { "unk00":"I", "unk04":"I", "unk08":"I", }},
    0x00002364 : {"name":"0x00002364", "id":0x00002364, "index":0xDB, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000236E : {"name":"0x0000236E", "id":0x0000236E, "index":0xDC, "size":3, 
                  "args": { "unk00":"I", "unk04":"I", }},
    0x00002378 : {"name":"0x00002378", "id":0x00002378, "index":0xDD, "size":2, 
                  "args": { "unk00":"I", }},
    0x00002382 : {"name":"0x00002382", "id":0x00002382, "index":0xDE, "size":1, 
                  "args": { }},
    0x0000238C : {"name":"0x0000238C", "id":0x0000238C, "index":0xDF, "size":2, 
                  "args": { "unk00":"I", }},
    0x00002396 : {"name":"0x00002396", "id":0x00002396, "index":0xE0, "size":1, 
                  "args": { }},
    0x00002350 : {"name":"0x00002350", "id":0x00002350, "index":0xE1, "size":2, 
                  "args": { "unk00":"I", }},
    0x0000235A : {"name":"0x0000235A", "id":0x0000235A, "index":0xE2, "size":1, 
                  "args": { }},
    0x000023A0 : {"name":"0x000023A0", "id":0x000023A0, "index":0xE3, "size":1, 
                  "args": { }},
    0x0001869F : {"name":"0x0001869F", "id":0x0001869F, "index":0xE4, "size":1, 
                  "args": { }},
}

OPCODES_SCRIPT |= {v["name"]:v for name,v in OPCODES_SCRIPT.items()}

class show_notification:
    args = OPCODES_SCRIPT[0x00000000]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(show_notification.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "msg_id":
                msg = read_string_file.get_string(30, arg)
                out_arg = f"0x{arg:X}: {msg}"
            elif arg_name == "s0":
                out_arg = f"0x{arg:X}"
                if arg in unit_defs:
                    out_arg += f" ({unit_defs[arg]})"
            elif arg_name == "s1":
                out_arg = f"0x{arg:X}"
                if arg in unit_defs:
                    out_arg += f" ({unit_defs[arg]})"
            elif arg_name == "s2":
                out_arg = f"0x{arg:X}"
                if arg in unit_defs:
                    out_arg += f" ({unit_defs[arg]})"
            elif arg_name == "s3":
                out_arg = f"0x{arg:X}"
                if arg in unit_defs:
                    out_arg += f" ({unit_defs[arg]})"
            elif arg_name == "unk14":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk18":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in show_notification!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = show_notification.args[name]
            if name == "msg_id":
                out_arg = int(arg.split(":",1)[0], 0)
            elif name == "s0":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s1":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s2":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s3":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "unk14":
                out_arg = int(arg, 0)
            elif name == "unk18":
                out_arg = int(arg, 0)
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in show_notification!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class play_speech:
    args = OPCODES_SCRIPT[0x0000000A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(play_speech.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "msg_id":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in play_speech!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = play_speech.args[name]
            if name == "msg_id":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in play_speech!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000014:
    args = OPCODES_SCRIPT[0x00000014]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000014.args.items()):
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
                print(f"Bad number of args in script_00000014!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000014.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000014!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000001E:
    args = OPCODES_SCRIPT[0x0000001E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000001E.args.items()):
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
                print(f"Bad number of args in script_0000001E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000001E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000001E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000028:
    args = OPCODES_SCRIPT[0x00000028]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000028.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000028!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000028.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000028!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000032:
    args = OPCODES_SCRIPT[0x00000032]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000032.args.items()):
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
                print(f"Bad number of args in script_00000032!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000032.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000032!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000003C:
    args = OPCODES_SCRIPT[0x0000003C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000003C.args.items()):
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
                print(f"Bad number of args in script_0000003C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000003C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000003C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000046:
    args = OPCODES_SCRIPT[0x00000046]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000046.args.items()):
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
                print(f"Bad number of args in script_00000046!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000046.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000046!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000050:
    args = OPCODES_SCRIPT[0x00000050]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000050.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000050!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000050.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000050!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000005A:
    args = OPCODES_SCRIPT[0x0000005A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00000064:
    args = OPCODES_SCRIPT[0x00000064]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000064.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000064!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000064.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000064!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class unit_ping:
    args = OPCODES_SCRIPT[0x000003E8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(unit_ping.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in unit_ping!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = unit_ping.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in unit_ping!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000003ED:
    args = OPCODES_SCRIPT[0x000003ED]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000003ED.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000003ED!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000003ED.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000003ED!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000003EF:
    args = OPCODES_SCRIPT[0x000003EF]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000003EF.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000003EF!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000003EF.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000003EF!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000003F2:
    args = OPCODES_SCRIPT[0x000003F2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000003F2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000003F2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000003F2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000003F2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000003FC:
    args = OPCODES_SCRIPT[0x000003FC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000003FC.args.items()):
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
                print(f"Bad number of args in script_000003FC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000003FC.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000003FC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000406:
    args = OPCODES_SCRIPT[0x00000406]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000406.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000406!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000406.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000406!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000410:
    args = OPCODES_SCRIPT[0x00000410]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000410.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000410!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000410.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000410!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000041A:
    args = OPCODES_SCRIPT[0x0000041A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000041A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000041A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000041A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000041A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000424:
    args = OPCODES_SCRIPT[0x00000424]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000424.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000424!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000424.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000424!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000042E:
    args = OPCODES_SCRIPT[0x0000042E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000042E.args.items()):
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
                print(f"Bad number of args in script_0000042E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000042E.args[name]
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
                print(f"Bad number of args in script_0000042E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000438:
    args = OPCODES_SCRIPT[0x00000438]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000438.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000438!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000438.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000438!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000442:
    args = OPCODES_SCRIPT[0x00000442]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000442.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000442!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000442.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000442!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000044C:
    args = OPCODES_SCRIPT[0x0000044C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000044C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000044C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000044C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000044C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000456:
    args = OPCODES_SCRIPT[0x00000456]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000456.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000456!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000456.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000456!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000045B:
    args = OPCODES_SCRIPT[0x0000045B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000045B.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000045B!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000045B.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000045B!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000460:
    args = OPCODES_SCRIPT[0x00000460]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000460.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000460!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000460.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000460!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000465:
    args = OPCODES_SCRIPT[0x00000465]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000465.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000465!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000465.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000465!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000046A:
    args = OPCODES_SCRIPT[0x0000046A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000046A.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000046A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000046A.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000046A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000474:
    args = OPCODES_SCRIPT[0x00000474]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000474.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000474!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000474.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000474!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000479:
    args = OPCODES_SCRIPT[0x00000479]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000479.args.items()):
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
                print(f"Bad number of args in script_00000479!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000479.args[name]
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
                print(f"Bad number of args in script_00000479!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000047E:
    args = OPCODES_SCRIPT[0x0000047E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000047E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000047E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000047E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000047E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000007D0:
    args = OPCODES_SCRIPT[0x000007D0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000007D0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000007D0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000007D0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000007D0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000007DA:
    args = OPCODES_SCRIPT[0x000007DA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000007DA.args.items()):
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
                print(f"Bad number of args in script_000007DA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000007DA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000007DA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000007E4:
    args = OPCODES_SCRIPT[0x000007E4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000007E4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000007E4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000007E4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000007E4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000007EE:
    args = OPCODES_SCRIPT[0x000007EE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000007EE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000007EE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000007EE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000007EE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000007F8:
    args = OPCODES_SCRIPT[0x000007F8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000007F8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000007F8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000007F8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000007F8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000802:
    args = OPCODES_SCRIPT[0x00000802]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000802.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000802!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000802.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000802!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class unit_set_active:
    args = OPCODES_SCRIPT[0x00000BB8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(unit_set_active.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in unit_set_active!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = unit_set_active.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in unit_set_active!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000BC2:
    args = OPCODES_SCRIPT[0x00000BC2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000BC2.args.items()):
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
                print(f"Bad number of args in script_00000BC2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000BC2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000BC2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000BC7:
    args = OPCODES_SCRIPT[0x00000BC7]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000BC7.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000BC7!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000BC7.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000BC7!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000BD6:
    args = OPCODES_SCRIPT[0x00000BD6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000BD6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000BD6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000BD6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000BD6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000BE0:
    args = OPCODES_SCRIPT[0x00000BE0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000BE0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000BE0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000BE0.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000BE0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000BE5:
    args = OPCODES_SCRIPT[0x00000BE5]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000BE5.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
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
                print(f"Bad number of args in script_00000BE5!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000BE5.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
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
                print(f"Bad number of args in script_00000BE5!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000BEA:
    args = OPCODES_SCRIPT[0x00000BEA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000BEA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000BEA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000BEA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000BEA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class unit_kill:
    args = OPCODES_SCRIPT[0x00000BF4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(unit_kill.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
            else:
                print(f"Bad number of args in unit_kill!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = unit_kill.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            else:
                print(f"Bad number of args in unit_kill!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000BFE:
    args = OPCODES_SCRIPT[0x00000BFE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000BFE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000BFE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000BFE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000BFE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C03:
    args = OPCODES_SCRIPT[0x00000C03]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C03.args.items()):
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
                print(f"Bad number of args in script_00000C03!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C03.args[name]
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
                print(f"Bad number of args in script_00000C03!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C08:
    args = OPCODES_SCRIPT[0x00000C08]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C08.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C08!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C08.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C08!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C0D:
    args = OPCODES_SCRIPT[0x00000C0D]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C0D.args.items()):
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
                print(f"Bad number of args in script_00000C0D!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C0D.args[name]
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
                print(f"Bad number of args in script_00000C0D!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C12:
    args = OPCODES_SCRIPT[0x00000C12]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C12.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C12!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C12.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C12!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C21:
    args = OPCODES_SCRIPT[0x00000C21]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C21.args.items()):
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
                print(f"Bad number of args in script_00000C21!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C21.args[name]
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
                print(f"Bad number of args in script_00000C21!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class unit_move:
    args = OPCODES_SCRIPT[0x00000C2B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(unit_move.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "target":
                if arg in unit_defs:
                    out_arg = f"0x{arg:X} ({unit_defs[arg]})"
                else:
                    out_arg = f"0x{arg:X} ()"
            elif arg_name == "x":
                out_arg = f"0x{arg:X}"
            elif arg_name == "y":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk18":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk28":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in unit_move!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = unit_move.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "target":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "x":
                out_arg = int(arg, 0)
            elif name == "y":
                out_arg = int(arg, 0)
            elif name == "unk18":
                out_arg = int(arg, 0)
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            elif name == "unk28":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in unit_move!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C30:
    args = OPCODES_SCRIPT[0x00000C30]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C30.args.items()):
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
                print(f"Bad number of args in script_00000C30!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C30.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C30!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C35:
    args = OPCODES_SCRIPT[0x00000C35]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C35.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk28":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C35!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C35.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            elif name == "unk28":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C35!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C3A:
    args = OPCODES_SCRIPT[0x00000C3A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C3A.args.items()):
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
                print(f"Bad number of args in script_00000C3A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C3A.args[name]
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
                print(f"Bad number of args in script_00000C3A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C3F:
    args = OPCODES_SCRIPT[0x00000C3F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C3F.args.items()):
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
                print(f"Bad number of args in script_00000C3F!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C3F.args[name]
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
                print(f"Bad number of args in script_00000C3F!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class unit_set_courage:
    args = OPCODES_SCRIPT[0x00000C44]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(unit_set_courage.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
            elif arg_name == "level":
                out_arg = arg
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in unit_set_courage!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = unit_set_courage.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "level":
                out_arg = arg
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in unit_set_courage!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C49:
    args = OPCODES_SCRIPT[0x00000C49]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C49.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C49!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C49.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C49!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C4E:
    args = OPCODES_SCRIPT[0x00000C4E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C4E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C4E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C4E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C4E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C58:
    args = OPCODES_SCRIPT[0x00000C58]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C58.args.items()):
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
                print(f"Bad number of args in script_00000C58!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C58.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C58!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C85:
    args = OPCODES_SCRIPT[0x00000C85]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C85.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C85!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C85.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C85!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class change_morale:
    args = OPCODES_SCRIPT[0x00000C8A]["args"]

    dirs = {
        # 0 does something weird, not sure what it is
        1: "Up",
        2: "Down",
    }
    dirs |= {v:n for n,v in dirs.items()}

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(change_morale.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "force":
                out_arg = arg
            elif arg_name == "dir":
                out_arg = change_morale.dirs[arg]
            elif arg_name == "amount":
                out_arg = arg
            elif arg_name == "unk0C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in change_morale!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = change_morale.args[name]
            if name == "force":
                out_arg = arg
            elif name == "dir":
                out_arg = change_morale.dirs[arg]
            elif name == "amount":
                out_arg = arg
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in change_morale!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C93:
    args = OPCODES_SCRIPT[0x00000C93]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C93.args.items()):
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
                print(f"Bad number of args in script_00000C93!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C93.args[name]
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
                print(f"Bad number of args in script_00000C93!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C94:
    args = OPCODES_SCRIPT[0x00000C94]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C94.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C94!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C94.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C94!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000C9E:
    args = OPCODES_SCRIPT[0x00000C9E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000C9E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000C9E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000C9E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000C9E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CA8:
    args = OPCODES_SCRIPT[0x00000CA8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CA8.args.items()):
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
                print(f"Bad number of args in script_00000CA8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CA8.args[name]
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
                print(f"Bad number of args in script_00000CA8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CB2:
    args = OPCODES_SCRIPT[0x00000CB2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CB2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000CB2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CB2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000CB2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CBC:
    args = OPCODES_SCRIPT[0x00000CBC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CBC.args.items()):
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
                print(f"Bad number of args in script_00000CBC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CBC.args[name]
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
                print(f"Bad number of args in script_00000CBC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CC6:
    args = OPCODES_SCRIPT[0x00000CC6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CC6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000CC6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CC6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000CC6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CD0:
    args = OPCODES_SCRIPT[0x00000CD0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CD0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000CD0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CD0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000CD0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CDA:
    args = OPCODES_SCRIPT[0x00000CDA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CDA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000CDA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CDA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000CDA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CE4:
    args = OPCODES_SCRIPT[0x00000CE4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CE4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000CE4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CE4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000CE4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CE9:
    args = OPCODES_SCRIPT[0x00000CE9]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CE9.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000CE9!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CE9.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000CE9!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class unit_change_name:
    args = OPCODES_SCRIPT[0x00000CEE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(unit_change_name.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                name = unit_defs[arg]
                out_arg = f"0x{arg:X} ({name})"
            elif arg_name == "name":
                out_arg = f"0x{arg:X} ({chars.char_id_to_name(arg)})"
            else:
                print(f"Bad number of args in unit_change_name!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = unit_change_name.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "name":
                out_arg = int(arg.split(" ",1)[0], 0)
            else:
                print(f"Bad number of args in unit_change_name!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000CF8:
    args = OPCODES_SCRIPT[0x00000CF8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000CF8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000CF8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000CF8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000CF8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D02:
    args = OPCODES_SCRIPT[0x00000D02]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D02.args.items()):
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
                print(f"Bad number of args in script_00000D02!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D02.args[name]
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
                print(f"Bad number of args in script_00000D02!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D07:
    args = OPCODES_SCRIPT[0x00000D07]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D07.args.items()):
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
                print(f"Bad number of args in script_00000D07!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D07.args[name]
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
                print(f"Bad number of args in script_00000D07!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D0C:
    args = OPCODES_SCRIPT[0x00000D0C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D0C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D0C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D0C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D0C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D16:
    args = OPCODES_SCRIPT[0x00000D16]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D16.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D16!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D16.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D16!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D20:
    args = OPCODES_SCRIPT[0x00000D20]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D20.args.items()):
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
                print(f"Bad number of args in script_00000D20!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D20.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D20!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D25:
    args = OPCODES_SCRIPT[0x00000D25]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D25.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D25!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D25.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D25!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D2A:
    args = OPCODES_SCRIPT[0x00000D2A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D2A.args.items()):
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
                print(f"Bad number of args in script_00000D2A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D2A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D2A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D34:
    args = OPCODES_SCRIPT[0x00000D34]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D34.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D34!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D34.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D34!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D3E:
    args = OPCODES_SCRIPT[0x00000D3E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D3E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D3E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D3E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D3E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D48:
    args = OPCODES_SCRIPT[0x00000D48]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D48.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D48!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D48.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D48!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D52:
    args = OPCODES_SCRIPT[0x00000D52]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D52.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D52!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D52.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D52!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D5C:
    args = OPCODES_SCRIPT[0x00000D5C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D5C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D5C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D5C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D5C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D66:
    args = OPCODES_SCRIPT[0x00000D66]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D66.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D66!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D66.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D66!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D6B:
    args = OPCODES_SCRIPT[0x00000D6B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D6B.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D6B!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D6B.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D6B!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D70:
    args = OPCODES_SCRIPT[0x00000D70]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D70.args.items()):
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
                print(f"Bad number of args in script_00000D70!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D70.args[name]
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
                print(f"Bad number of args in script_00000D70!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D7A:
    args = OPCODES_SCRIPT[0x00000D7A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D7A.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D7A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D7A.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D7A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D7B:
    args = OPCODES_SCRIPT[0x00000D7B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D7B.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D7B!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D7B.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D7B!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D84:
    args = OPCODES_SCRIPT[0x00000D84]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D84.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D84!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D84.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D84!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D8E:
    args = OPCODES_SCRIPT[0x00000D8E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D8E.args.items()):
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
                print(f"Bad number of args in script_00000D8E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D8E.args[name]
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
                print(f"Bad number of args in script_00000D8E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D98:
    args = OPCODES_SCRIPT[0x00000D98]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D98.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D98!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D98.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D98!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D9D:
    args = OPCODES_SCRIPT[0x00000D9D]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D9D.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk28":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk2C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk30":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk34":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk38":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk3C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk40":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D9D!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D9D.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            elif name == "unk28":
                out_arg = int(arg, 0)
            elif name == "unk2C":
                out_arg = int(arg, 0)
            elif name == "unk30":
                out_arg = int(arg, 0)
            elif name == "unk34":
                out_arg = int(arg, 0)
            elif name == "unk38":
                out_arg = int(arg, 0)
            elif name == "unk3C":
                out_arg = int(arg, 0)
            elif name == "unk40":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D9D!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000D9F:
    args = OPCODES_SCRIPT[0x00000D9F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000D9F.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000D9F!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000D9F.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000D9F!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DA2:
    args = OPCODES_SCRIPT[0x00000DA2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DA2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000DA2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DA2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DA2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DAC:
    args = OPCODES_SCRIPT[0x00000DAC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DAC.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000DAC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DAC.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DAC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DB6:
    args = OPCODES_SCRIPT[0x00000DB6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DB6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000DB6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DB6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DB6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DC0:
    args = OPCODES_SCRIPT[0x00000DC0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DC0.args.items()):
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
                print(f"Bad number of args in script_00000DC0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DC0.args[name]
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
                print(f"Bad number of args in script_00000DC0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DCA:
    args = OPCODES_SCRIPT[0x00000DCA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DCA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000DCA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DCA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DCA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DD4:
    args = OPCODES_SCRIPT[0x00000DD4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DD4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000DD4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DD4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DD4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DDE:
    args = OPCODES_SCRIPT[0x00000DDE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DDE.args.items()):
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
                print(f"Bad number of args in script_00000DDE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DDE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DDE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DE8:
    args = OPCODES_SCRIPT[0x00000DE8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DE8.args.items()):
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
                print(f"Bad number of args in script_00000DE8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DE8.args[name]
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
                print(f"Bad number of args in script_00000DE8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DF2:
    args = OPCODES_SCRIPT[0x00000DF2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DF2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000DF2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DF2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DF2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000DFC:
    args = OPCODES_SCRIPT[0x00000DFC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000DFC.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000DFC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000DFC.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000DFC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000E01:
    args = OPCODES_SCRIPT[0x00000E01]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000E01.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000E01!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000E01.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000E01!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000E06:
    args = OPCODES_SCRIPT[0x00000E06]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000E06.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000E06!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000E06.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000E06!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000E0B:
    args = OPCODES_SCRIPT[0x00000E0B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000E0B.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000E0B!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000E0B.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000E0B!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000E10:
    args = OPCODES_SCRIPT[0x00000E10]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000E10.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000E10!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000E10.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000E10!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FA0:
    args = OPCODES_SCRIPT[0x00000FA0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FA0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FA0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FA0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FA0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FA5:
    args = OPCODES_SCRIPT[0x00000FA5]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FA5.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FA5!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FA5.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FA5!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FAA:
    args = OPCODES_SCRIPT[0x00000FAA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FAA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FAA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FAA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FAA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FAD:
    args = OPCODES_SCRIPT[0x00000FAD]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FAD.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FAD!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FAD.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FAD!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FAE:
    args = OPCODES_SCRIPT[0x00000FAE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FAE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FAE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FAE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FAE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FAF:
    args = OPCODES_SCRIPT[0x00000FAF]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FAF.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FAF!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FAF.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FAF!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FB4:
    args = OPCODES_SCRIPT[0x00000FB4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FB4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FB4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FB4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FB4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FB5:
    args = OPCODES_SCRIPT[0x00000FB5]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FB5.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FB5!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FB5.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FB5!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FB7:
    args = OPCODES_SCRIPT[0x00000FB7]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FB7.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FB7!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FB7.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FB7!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FB9:
    args = OPCODES_SCRIPT[0x00000FB9]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FB9.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FB9!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FB9.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FB9!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FBE:
    args = OPCODES_SCRIPT[0x00000FBE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FBE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FBE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FBE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FBE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FE6:
    args = OPCODES_SCRIPT[0x00000FE6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FE6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FE6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FE6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FE6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FF0:
    args = OPCODES_SCRIPT[0x00000FF0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FF0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FF0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FF0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FF0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FF5:
    args = OPCODES_SCRIPT[0x00000FF5]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FF5.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00000FF5!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FF5.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00000FF5!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00000FFA:
    args = OPCODES_SCRIPT[0x00000FFA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00000FFA.args.items()):
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
                print(f"Bad number of args in script_00000FFA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00000FFA.args[name]
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
                print(f"Bad number of args in script_00000FFA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001004:
    args = OPCODES_SCRIPT[0x00001004]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001004.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001004!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001004.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001004!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000100E:
    args = OPCODES_SCRIPT[0x0000100E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000100E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000100E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000100E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000100E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001018:
    args = OPCODES_SCRIPT[0x00001018]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001018.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001018!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001018.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001018!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001022:
    args = OPCODES_SCRIPT[0x00001022]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001022.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001022!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001022.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001022!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001027:
    args = OPCODES_SCRIPT[0x00001027]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001027.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001027!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001027.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001027!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000102C:
    args = OPCODES_SCRIPT[0x0000102C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000102C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000102C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000102C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000102C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001036:
    args = OPCODES_SCRIPT[0x00001036]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001036.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001036!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001036.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001036!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001040:
    args = OPCODES_SCRIPT[0x00001040]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001040.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001040!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001040.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001040!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000104A:
    args = OPCODES_SCRIPT[0x0000104A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000104A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000104A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000104A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000104A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000104F:
    args = OPCODES_SCRIPT[0x0000104F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000104F.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000104F!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000104F.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000104F!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001054:
    args = OPCODES_SCRIPT[0x00001054]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001054.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001054!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001054.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001054!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000105E:
    args = OPCODES_SCRIPT[0x0000105E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000105E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000105E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000105E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000105E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001068:
    args = OPCODES_SCRIPT[0x00001068]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001068.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001068!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001068.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001068!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001072:
    args = OPCODES_SCRIPT[0x00001072]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001072.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001072!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001072.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001072!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000107C:
    args = OPCODES_SCRIPT[0x0000107C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000107C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000107C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000107C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000107C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001388:
    args = OPCODES_SCRIPT[0x00001388]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001388.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001388!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001388.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001388!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001392:
    args = OPCODES_SCRIPT[0x00001392]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001392.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001392!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001392.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001392!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000139C:
    args = OPCODES_SCRIPT[0x0000139C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000139C.args.items()):
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
                print(f"Bad number of args in script_0000139C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000139C.args[name]
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
                print(f"Bad number of args in script_0000139C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013A1:
    args = OPCODES_SCRIPT[0x000013A1]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013A1.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013A1!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013A1.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013A1!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013A4:
    args = OPCODES_SCRIPT[0x000013A4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013A4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013A4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013A4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013A4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013A6:
    args = OPCODES_SCRIPT[0x000013A6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013A6.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013A6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013A6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013A6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013B0:
    args = OPCODES_SCRIPT[0x000013B0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013B0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013B0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013B0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013B0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013BA:
    args = OPCODES_SCRIPT[0x000013BA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013BA.args.items()):
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
                print(f"Bad number of args in script_000013BA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013BA.args[name]
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
                print(f"Bad number of args in script_000013BA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013C4:
    args = OPCODES_SCRIPT[0x000013C4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_000013CE:
    args = OPCODES_SCRIPT[0x000013CE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013CE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013CE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013CE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013CE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013D8:
    args = OPCODES_SCRIPT[0x000013D8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013D8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013D8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013D8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013D8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013E2:
    args = OPCODES_SCRIPT[0x000013E2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013E2.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013E2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013E2.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013E2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013E5:
    args = OPCODES_SCRIPT[0x000013E5]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013E5.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013E5!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013E5.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013E5!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013E7:
    args = OPCODES_SCRIPT[0x000013E7]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013E7.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013E7!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013E7.args[name]
            if name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013E7!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013EC:
    args = OPCODES_SCRIPT[0x000013EC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000013EC.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000013EC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000013EC.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000013EC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000013F6:
    args = OPCODES_SCRIPT[0x000013F6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00001400:
    args = OPCODES_SCRIPT[0x00001400]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001400.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001400!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001400.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001400!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000140A:
    args = OPCODES_SCRIPT[0x0000140A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000140A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000140A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000140A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000140A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000140F:
    args = OPCODES_SCRIPT[0x0000140F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00001414:
    args = OPCODES_SCRIPT[0x00001414]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001414.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001414!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001414.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001414!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000141E:
    args = OPCODES_SCRIPT[0x0000141E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000141E.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000141E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000141E.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000141E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001428:
    args = OPCODES_SCRIPT[0x00001428]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001428.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001428!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001428.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001428!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001432:
    args = OPCODES_SCRIPT[0x00001432]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001432.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001432!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001432.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001432!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000143C:
    args = OPCODES_SCRIPT[0x0000143C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000143C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000143C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000143C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000143C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001446:
    args = OPCODES_SCRIPT[0x00001446]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00001450:
    args = OPCODES_SCRIPT[0x00001450]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001450.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001450!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001450.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001450!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001770:
    args = OPCODES_SCRIPT[0x00001770]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001770.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001770!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001770.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001770!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001775:
    args = OPCODES_SCRIPT[0x00001775]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001775.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unit_id":
                out_arg = f"0x{arg:X} ({unit_defs[arg]})"
            else:
                print(f"Bad number of args in script_00001775!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001775.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unit_id":
                out_arg = int(arg.split(" ",1)[0], 0)
            else:
                print(f"Bad number of args in script_00001775!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000177A:
    args = OPCODES_SCRIPT[0x0000177A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000177A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000177A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000177A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000177A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001784:
    args = OPCODES_SCRIPT[0x00001784]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001784.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001784!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001784.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001784!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000178E:
    args = OPCODES_SCRIPT[0x0000178E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000178E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000178E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000178E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000178E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001798:
    args = OPCODES_SCRIPT[0x00001798]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001798.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001798!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001798.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001798!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000017A2:
    args = OPCODES_SCRIPT[0x000017A2]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000017A2.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_000017A2!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000017A2.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_000017A2!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_000017AC:
    args = OPCODES_SCRIPT[0x000017AC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_000017AC.args.items()):
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
                print(f"Bad number of args in script_000017AC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_000017AC.args[name]
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
                print(f"Bad number of args in script_000017AC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001F40:
    args = OPCODES_SCRIPT[0x00001F40]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001F40.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001F40!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001F40.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001F40!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class defeat_condition:
    args = OPCODES_SCRIPT[0x00001F4A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(defeat_condition.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "string":
                out_arg = f"{read_string_file.get_string(32, arg)}"
            elif arg_name == "s0":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            elif arg_name == "s1":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            elif arg_name == "s2":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            elif arg_name == "s3":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            else:
                print(f"Bad number of args in defeat_condition!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = defeat_condition.args[name]
            if name == "string":
                if type(arg) == int:
                    out_arg = arg
                else:
                    out_arg = read_string_file.get_index(32, arg)
            elif name == "s0":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s1":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s2":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s3":
                out_arg = int(arg.split(" ",1)[0], 0)
            else:
                print(f"Bad number of args in defeat_condition!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class victory_condition:
    args = OPCODES_SCRIPT[0x00001F54]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(victory_condition.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "string":
                out_arg = f"{read_string_file.get_string(31, arg)}"
            elif arg_name == "s0":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            elif arg_name == "s1":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            elif arg_name == "s2":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            elif arg_name == "s3":
                out_arg = f"0x{arg:X}"

                name = chars.char_id_to_name(arg)
                out_arg += f" ({name})"
            else:
                print(f"Bad number of args in victory_condition!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = victory_condition.args[name]
            if name == "string":
                if type(arg) == int:
                    out_arg = arg
                else:
                    out_arg = read_string_file.get_index(31, arg)
            elif name == "s0":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s1":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s2":
                out_arg = int(arg.split(" ",1)[0], 0)
            elif name == "s3":
                out_arg = int(arg.split(" ",1)[0], 0)
            else:
                print(f"Bad number of args in victory_condition!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001F68:
    args = OPCODES_SCRIPT[0x00001F68]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001F68.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001F68!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001F68.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001F68!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001F7C:
    args = OPCODES_SCRIPT[0x00001F7C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001F7C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001F7C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001F7C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001F7C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001F86:
    args = OPCODES_SCRIPT[0x00001F86]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001F86.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001F86!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001F86.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001F86!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001F90:
    args = OPCODES_SCRIPT[0x00001F90]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001F90.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001F90!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001F90.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001F90!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001F9A:
    args = OPCODES_SCRIPT[0x00001F9A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001F9A.args.items()):
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
                print(f"Bad number of args in script_00001F9A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001F9A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001F9A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FA4:
    args = OPCODES_SCRIPT[0x00001FA4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FA4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001FA4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FA4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FA4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FAE:
    args = OPCODES_SCRIPT[0x00001FAE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00001FB3:
    args = OPCODES_SCRIPT[0x00001FB3]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00001FB8:
    args = OPCODES_SCRIPT[0x00001FB8]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FB8.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001FB8!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FB8.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FB8!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class end_battle:
    args = OPCODES_SCRIPT[0x00001FC2]["args"]

    state = {
        0: "Victory",
        1: "Defeat",
    }
    state |= {n:v for v,n in state.items()}

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(end_battle.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "state":
                out_arg = f"{end_battle.state[arg]}"
            else:
                print(f"Bad number of args in end_battle!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = end_battle.args[name]
            if name == "state":
                out_arg = end_battle.state[arg]
            else:
                print(f"Bad number of args in end_battle!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FCC:
    args = OPCODES_SCRIPT[0x00001FCC]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FCC.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001FCC!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FCC.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FCC!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FD6:
    args = OPCODES_SCRIPT[0x00001FD6]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FD6.args.items()):
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
                print(f"Bad number of args in script_00001FD6!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FD6.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FD6!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FE0:
    args = OPCODES_SCRIPT[0x00001FE0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FE0.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001FE0!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FE0.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FE0!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FEA:
    args = OPCODES_SCRIPT[0x00001FEA]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FEA.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001FEA!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FEA.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FEA!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FF4:
    args = OPCODES_SCRIPT[0x00001FF4]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FF4.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001FF4!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FF4.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FF4!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00001FFE:
    args = OPCODES_SCRIPT[0x00001FFE]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00001FFE.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00001FFE!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00001FFE.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00001FFE!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002008:
    args = OPCODES_SCRIPT[0x00002008]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002008.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002008!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002008.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002008!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002012:
    args = OPCODES_SCRIPT[0x00002012]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002012.args.items()):
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
                print(f"Bad number of args in script_00002012!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002012.args[name]
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
                print(f"Bad number of args in script_00002012!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000201C:
    args = OPCODES_SCRIPT[0x0000201C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000201C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000201C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000201C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000201C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002026:
    args = OPCODES_SCRIPT[0x00002026]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002026.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002026!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002026.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002026!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002030:
    args = OPCODES_SCRIPT[0x00002030]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002030.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002030!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002030.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002030!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000203A:
    args = OPCODES_SCRIPT[0x0000203A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000203A.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000203A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000203A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000203A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002044:
    args = OPCODES_SCRIPT[0x00002044]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002044.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002044!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002044.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002044!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000204E:
    args = OPCODES_SCRIPT[0x0000204E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00002058:
    args = OPCODES_SCRIPT[0x00002058]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00002062:
    args = OPCODES_SCRIPT[0x00002062]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002062.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002062!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002062.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002062!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000206C:
    args = OPCODES_SCRIPT[0x0000206C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000206C.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk28":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000206C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000206C.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            elif name == "unk28":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000206C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002076:
    args = OPCODES_SCRIPT[0x00002076]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002076.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002076!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002076.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002076!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000207B:
    args = OPCODES_SCRIPT[0x0000207B]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000207B.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000207B!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000207B.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000207B!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002080:
    args = OPCODES_SCRIPT[0x00002080]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002080.args.items()):
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
                print(f"Bad number of args in script_00002080!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002080.args[name]
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
                print(f"Bad number of args in script_00002080!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000208A:
    args = OPCODES_SCRIPT[0x0000208A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000208A.args.items()):
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
                print(f"Bad number of args in script_0000208A!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000208A.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000208A!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000208F:
    args = OPCODES_SCRIPT[0x0000208F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000208F.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000208F!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000208F.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000208F!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002090:
    args = OPCODES_SCRIPT[0x00002090]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002090.args.items()):
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
            elif arg_name == "unk1C":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk20":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk24":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002090!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002090.args[name]
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
            elif name == "unk1C":
                out_arg = int(arg, 0)
            elif name == "unk20":
                out_arg = int(arg, 0)
            elif name == "unk24":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002090!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002094:
    args = OPCODES_SCRIPT[0x00002094]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002094.args.items()):
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
                print(f"Bad number of args in script_00002094!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002094.args[name]
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
                print(f"Bad number of args in script_00002094!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000209E:
    args = OPCODES_SCRIPT[0x0000209E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000209E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk08":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000209E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000209E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000209E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002328:
    args = OPCODES_SCRIPT[0x00002328]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00002332:
    args = OPCODES_SCRIPT[0x00002332]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_0000233C:
    args = OPCODES_SCRIPT[0x0000233C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000233C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000233C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000233C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000233C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002341:
    args = OPCODES_SCRIPT[0x00002341]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002341.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002341!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002341.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002341!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002346:
    args = OPCODES_SCRIPT[0x00002346]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002346.args.items()):
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
                print(f"Bad number of args in script_00002346!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002346.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            elif name == "unk08":
                out_arg = int(arg, 0)
            elif name == "unk0C":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002346!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002350:
    args = OPCODES_SCRIPT[0x00002350]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002350.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002350!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002350.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002350!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000235A:
    args = OPCODES_SCRIPT[0x0000235A]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_00002364:
    args = OPCODES_SCRIPT[0x00002364]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002364.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002364!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002364.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002364!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_0000236E:
    args = OPCODES_SCRIPT[0x0000236E]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000236E.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            elif arg_name == "unk04":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000236E!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000236E.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            elif name == "unk04":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000236E!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002378:
    args = OPCODES_SCRIPT[0x00002378]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_00002378.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_00002378!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_00002378.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_00002378!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002382:
    args = OPCODES_SCRIPT[0x00002382]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_0000238C:
    args = OPCODES_SCRIPT[0x0000238C]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        for i, (arg_name, arg_type) in enumerate(script_0000238C.args.items()):
            arg = struct.unpack_from(f"<{arg_type}", script, pos)[0]
            pos += 0x4
            if arg_name == "unk00":
                out_arg = f"0x{arg:X}"
            else:
                print(f"Bad number of args in script_0000238C!")
                exit()
            out_args[arg_name] = out_arg
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        for name, arg in opcode["args"].items():
            arg_type = script_0000238C.args[name]
            if name == "unk00":
                out_arg = int(arg, 0)
            else:
                print(f"Bad number of args in script_0000238C!")
                exit()
            out_data.append(struct.pack(f"<{arg_type}", out_arg))
        return b"".join(out_data)
        
class script_00002396:
    args = OPCODES_SCRIPT[0x00002396]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_000023A0:
    args = OPCODES_SCRIPT[0x000023A0]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        
class script_0001869F:
    args = OPCODES_SCRIPT[0x0001869F]["args"]

    def decompile(script, pos, unit_defs):
        out_args = {}
        return out_args

    def compile(opcode, unit_defs):
        out_data = []
        return b"".join(out_data)
        

HANDLERS_SCRIPT = {
    0x00000000:show_notification,
    0x0000000A:play_speech,
    0x00000014:script_00000014,
    0x0000001E:script_0000001E,
    0x00000028:script_00000028,
    0x00000032:script_00000032,
    0x0000003C:script_0000003C,
    0x00000046:script_00000046,
    0x00000050:script_00000050,
    0x0000005A:script_0000005A,
    0x00000064:script_00000064,
    0x000003E8:unit_ping,
    0x000003ED:script_000003ED,
    0x000003EF:script_000003EF,
    0x000003F2:script_000003F2,
    0x000003FC:script_000003FC,
    0x00000406:script_00000406,
    0x00000410:script_00000410,
    0x0000041A:script_0000041A,
    0x00000424:script_00000424,
    0x0000042E:script_0000042E,
    0x00000438:script_00000438,
    0x00000442:script_00000442,
    0x0000044C:script_0000044C,
    0x00000456:script_00000456,
    0x0000045B:script_0000045B,
    0x00000460:script_00000460,
    0x00000465:script_00000465,
    0x0000046A:script_0000046A,
    0x00000474:script_00000474,
    0x00000479:script_00000479,
    0x0000047E:script_0000047E,
    0x000007D0:script_000007D0,
    0x000007DA:script_000007DA,
    0x000007E4:script_000007E4,
    0x000007EE:script_000007EE,
    0x000007F8:script_000007F8,
    0x00000802:script_00000802,
    0x00000BB8:unit_set_active,
    0x00000BC2:script_00000BC2,
    0x00000BC7:script_00000BC7,
    0x00000BD6:script_00000BD6,
    0x00000BE0:script_00000BE0,
    0x00000BE5:script_00000BE5,
    0x00000BEA:script_00000BEA,
    0x00000BF4:unit_kill,
    0x00000BFE:script_00000BFE,
    0x00000C03:script_00000C03,
    0x00000C08:script_00000C08,
    0x00000C0D:script_00000C0D,
    0x00000C12:script_00000C12,
    0x00000C21:script_00000C21,
    0x00000C2B:unit_move,
    0x00000C30:script_00000C30,
    0x00000C35:script_00000C35,
    0x00000C3A:script_00000C3A,
    0x00000C3F:script_00000C3F,
    0x00000C44:unit_set_courage,
    0x00000C49:script_00000C49,
    0x00000C4E:script_00000C4E,
    0x00000C58:script_00000C58,
    0x00000C85:script_00000C85,
    0x00000C8A:change_morale,
    0x00000C93:script_00000C93,
    0x00000C94:script_00000C94,
    0x00000C9E:script_00000C9E,
    0x00000CA8:script_00000CA8,
    0x00000CB2:script_00000CB2,
    0x00000CBC:script_00000CBC,
    0x00000CC6:script_00000CC6,
    0x00000CD0:script_00000CD0,
    0x00000CDA:script_00000CDA,
    0x00000CE4:script_00000CE4,
    0x00000CE9:script_00000CE9,
    0x00000CEE:unit_change_name,
    0x00000CF8:script_00000CF8,
    0x00000D02:script_00000D02,
    0x00000D07:script_00000D07,
    0x00000D0C:script_00000D0C,
    0x00000D16:script_00000D16,
    0x00000D20:script_00000D20,
    0x00000D25:script_00000D25,
    0x00000D2A:script_00000D2A,
    0x00000D34:script_00000D34,
    0x00000D3E:script_00000D3E,
    0x00000D48:script_00000D48,
    0x00000D52:script_00000D52,
    0x00000D5C:script_00000D5C,
    0x00000D66:script_00000D66,
    0x00000D6B:script_00000D6B,
    0x00000D70:script_00000D70,
    0x00000D7A:script_00000D7A,
    0x00000D7B:script_00000D7B,
    0x00000D84:script_00000D84,
    0x00000D8E:script_00000D8E,
    0x00000D98:script_00000D98,
    0x00000D9D:script_00000D9D,
    0x00000D9F:script_00000D9F,
    0x00000DA2:script_00000DA2,
    0x00000DAC:script_00000DAC,
    0x00000DB6:script_00000DB6,
    0x00000DC0:script_00000DC0,
    0x00000DCA:script_00000DCA,
    0x00000DD4:script_00000DD4,
    0x00000DDE:script_00000DDE,
    0x00000DE8:script_00000DE8,
    0x00000DF2:script_00000DF2,
    0x00000DFC:script_00000DFC,
    0x00000E01:script_00000E01,
    0x00000E06:script_00000E06,
    0x00000E0B:script_00000E0B,
    0x00000E10:script_00000E10,
    0x00000FA0:script_00000FA0,
    0x00000FA5:script_00000FA5,
    0x00000FAA:script_00000FAA,
    0x00000FAD:script_00000FAD,
    0x00000FAE:script_00000FAE,
    0x00000FAF:script_00000FAF,
    0x00000FB4:script_00000FB4,
    0x00000FB5:script_00000FB5,
    0x00000FB7:script_00000FB7,
    0x00000FB9:script_00000FB9,
    0x00000FBE:script_00000FBE,
    0x00000FE6:script_00000FE6,
    0x00000FF0:script_00000FF0,
    0x00000FF5:script_00000FF5,
    0x00000FFA:script_00000FFA,
    0x00001004:script_00001004,
    0x0000100E:script_0000100E,
    0x00001018:script_00001018,
    0x00001022:script_00001022,
    0x00001027:script_00001027,
    0x0000102C:script_0000102C,
    0x00001036:script_00001036,
    0x00001040:script_00001040,
    0x0000104A:script_0000104A,
    0x0000104F:script_0000104F,
    0x00001054:script_00001054,
    0x0000105E:script_0000105E,
    0x00001068:script_00001068,
    0x00001072:script_00001072,
    0x0000107C:script_0000107C,
    0x00001388:script_00001388,
    0x00001392:script_00001392,
    0x0000139C:script_0000139C,
    0x000013A1:script_000013A1,
    0x000013A4:script_000013A4,
    0x000013A6:script_000013A6,
    0x000013B0:script_000013B0,
    0x000013BA:script_000013BA,
    0x000013C4:script_000013C4,
    0x000013CE:script_000013CE,
    0x000013D8:script_000013D8,
    0x000013E2:script_000013E2,
    0x000013E5:script_000013E5,
    0x000013E7:script_000013E7,
    0x000013EC:script_000013EC,
    0x000013F6:script_000013F6,
    0x00001400:script_00001400,
    0x0000140A:script_0000140A,
    0x0000140F:script_0000140F,
    0x00001414:script_00001414,
    0x0000141E:script_0000141E,
    0x00001428:script_00001428,
    0x00001432:script_00001432,
    0x0000143C:script_0000143C,
    0x00001446:script_00001446,
    0x00001450:script_00001450,
    0x00001770:script_00001770,
    0x00001775:script_00001775,
    0x0000177A:script_0000177A,
    0x00001784:script_00001784,
    0x0000178E:script_0000178E,
    0x00001798:script_00001798,
    0x000017A2:script_000017A2,
    0x000017AC:script_000017AC,
    0x00001F40:script_00001F40,
    0x00001F4A:defeat_condition,
    0x00001F54:victory_condition,
    0x00001F68:script_00001F68,
    0x00001F7C:script_00001F7C,
    0x00001F86:script_00001F86,
    0x00001F90:script_00001F90,
    0x00001F9A:script_00001F9A,
    0x00001FA4:script_00001FA4,
    0x00001FAE:script_00001FAE,
    0x00001FB3:script_00001FB3,
    0x00001FB8:script_00001FB8,
    0x00001FC2:end_battle,
    0x00001FCC:script_00001FCC,
    0x00001FD6:script_00001FD6,
    0x00001FE0:script_00001FE0,
    0x00001FEA:script_00001FEA,
    0x00001FF4:script_00001FF4,
    0x00001FFE:script_00001FFE,
    0x00002008:script_00002008,
    0x00002012:script_00002012,
    0x0000201C:script_0000201C,
    0x00002026:script_00002026,
    0x00002030:script_00002030,
    0x0000203A:script_0000203A,
    0x00002044:script_00002044,
    0x0000204E:script_0000204E,
    0x00002058:script_00002058,
    0x00002062:script_00002062,
    0x0000206C:script_0000206C,
    0x00002076:script_00002076,
    0x0000207B:script_0000207B,
    0x00002080:script_00002080,
    0x0000208A:script_0000208A,
    0x0000208F:script_0000208F,
    0x00002090:script_00002090,
    0x00002094:script_00002094,
    0x0000209E:script_0000209E,
    0x00002328:script_00002328,
    0x00002332:script_00002332,
    0x0000233C:script_0000233C,
    0x00002341:script_00002341,
    0x00002346:script_00002346,
    0x00002350:script_00002350,
    0x0000235A:script_0000235A,
    0x00002364:script_00002364,
    0x0000236E:script_0000236E,
    0x00002378:script_00002378,
    0x00002382:script_00002382,
    0x0000238C:script_0000238C,
    0x00002396:script_00002396,
    0x000023A0:script_000023A0,
    0x0001869F:script_0001869F,
}
