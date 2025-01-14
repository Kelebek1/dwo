import sys
import struct
from pathlib import Path
from Crypto.Cipher import Blowfish

EXTRACT_FILES = True

def get_base_ktsr_pos(f):
    f.seek(0, 0)
    magic_test = struct.unpack_from("4s", f.read(0x4))[0]

    match magic_test:
        case b"IDRK":
            f.seek(0x48, 0)
            magic_test = struct.unpack_from("4s", f.read(0x4))[0]
            assert magic_test == b"KTSR"
            return 0x48

        case b"TSRS":
            f.seek(0x10, 0)
            magic_test = struct.unpack_from("4s", f.read(0x4))[0]
            assert magic_test == b"KTSR"
            return 0x10

        case b"ASRS":
            f.seek(0x10, 0)
            magic_test = struct.unpack_from("4s", f.read(0x4))[0]
            assert magic_test == b"KTSR"
            return 0x10

        case b"KTSR":
            return 0x0

        case _:
            print(f"Unable to determine file magic!")
            exit()

    return 0x0

ENCRYPTED_STREAMS = {}
def build_encrypted_streams():
    in_path = Path.cwd()

    files = list(Path.rglob(in_path, "*.file"))

    #for file in files:
    #    print(file)
    #exit()

    for file in files:
        if file.stat().st_size < 0x30:
            continue
        with open(file, "rb") as f:
            base_pos = get_base_ktsr_pos(f)
            pos = base_pos

            f.seek(pos + 0x18, 0)
            file_size = struct.unpack_from("<I", f.read(0x4))[0]
            
            f.seek(pos + 0x20, 0)
            key_size = f.read(1)[0]
            key = f.read(key_size)

            end = pos + file_size

            pos += 0x40
            while pos < end:
                f.seek(pos, 0)

                type = struct.unpack_from(">I", f.read(0x4))[0]
                size= struct.unpack_from("<I", f.read(0x4))[0]
                id = struct.unpack_from(">I", f.read(0x4))[0]

                match type:
                    case 0x09D4F415:
                        ENCRYPTED_STREAMS[id] = {"file":file, "key":key, "base_pos":base_pos}

                pos += size


    #for i,s in ENCRYPTED_STREAMS.items():
    #    if "DLC" in str(s["file"]):
    #        print(hex(i), s)
    #print(ENCRYPTED_STREAMS)
    #exit()

def read_name(f):
    out_name = b""
    while (c := f.read(1)) != b"\x00":
        out_name += c
    return out_name.decode("utf8")

def decrypt_name(f, seed):
    decrypted_name = bytearray()

    while True:
        seed = 0x343FD * seed + 0x269EC3

        char = ord(f.read(1)) ^ ((seed >> 0x10) & 0xFF)
        if char == 0x00:
            break;

        decrypted_name.append(char)

    return decrypted_name.decode("utf8")

build_encrypted_streams()

in_path = Path(sys.argv[1])

if not in_path.is_file():
    files = [f for f in in_path.glob("*.asrs")]
    files.extend([f for f in in_path.glob("*.file")])
else:
    files = [in_path]

for file in files:
    print(f"Parsing {file}")

    with open(file, "rb") as f:
        pos = get_base_ktsr_pos(f)
        f.seek(pos, 0)

        magic, ktsr_type, ktsr_ver, ktsr_flags, ktsr_platform, audio_id, \
        unk10, unk14, ktsr_size1, ktsr_size2, \
        unk20, unk24 = struct.unpack_from("<4sIHBBI IIII II", f.read(0x28))

        assert magic == b"KTSR", f"Bad magic at 0x{pos:X} -- expected KTSR, got {magic}"

        #print(hex(ktsr_size1))

        pos += 0x40
        count = 0
        while pos < ktsr_size1:
            f.seek(pos, 0)
            #print(f"pos 0x{pos:X}")

            type = struct.unpack_from(">I", f.read(0x4))[0]
            size = struct.unpack_from("<I", f.read(0x4))[0]

            match type:
                case 0x09D4F415:
                    stream_id = struct.unpack_from(">I", f.read(0x4))[0]
                    offset, data_size = struct.unpack_from("<II", f.read(0x8))
                    unk14, unk18, unk1C = struct.unpack_from("<III", f.read(0xC))
                    print(f"{count} at 0x{pos:X} -- type 0x{type:X} size 0x{size:X} stream_id 0x{stream_id:X} offset 0x{offset:X} data_size 0x{data_size:X} unk14 0x{unk14:X}, unk18 0x{unk18:X}, unk1C 0x{unk1C:X}")

                    f.seek(0, 0)
                    assert f.read(4) == b"IDRK", f"Bad file for type 0x09D4F415!"

                    f.seek(0x24, 0)
                    tid = struct.unpack_from("<I", f.read(4))[0] & 0xFFFFFFFF

                    """
                    if EXTRACT_FILES and stream_id in ENCRYPTED_STREAMS:
                        stream_data = ENCRYPTED_STREAMS[stream_id]
                        #print(f"\t\tIN ENCRYPTED {stream_data}")

                        f.seek(pos + offset, 0)
                        decrypt_aligned_size = data_size
                        while decrypt_aligned_size % 0x10:
                            decrypt_aligned_size += 1
                        audio_data = f.read(decrypt_aligned_size)

                        bf = Blowfish.new(stream_data["key"], Blowfish.MODE_ECB)
                        audio_data = bf.decrypt(audio_data)[:data_size]

                        decrypt_out_path = Path(str(file.with_suffix("")) + "_out")
                        #print(decrypt_out_path / f"{count}_{stream_id:x}.KA1A")
                        decrypt_out_path.mkdir(parents=True, exist_ok=True)
                        (decrypt_out_path / f"{count}_0x{tid:x}.ka1a").write_bytes(audio_data)
                    """
                
                case 0xBD888C36:
                    stream_id = struct.unpack_from(">I", f.read(0x4))[0]
                    flags = struct.unpack_from("<I", f.read(0x4))[0]
                    unk10, unk14, unk18, unk1C, unk20, unk24 = struct.unpack_from("<6I", f.read(6 * 4))
                    name_offset = struct.unpack_from("<I", f.read(0x4))[0]

                    print(f"{count} at 0x{pos:X} -- type 0x{type:X} size 0x{size:X} stream_id 0x{stream_id:X} flags 0x{flags:X} unk10 0x{unk10:X} unk14 0x{unk14:X} unk18 0x{unk18:X} unk1C 0x{unk1C:X} unk20 0x{unk20:X} unk24 0x{unk24:X}", end="")

                    if name_offset:
                        name_offset += pos
                        f.seek(name_offset, 0)

                        if flags & 0x200:
                            name = decrypt_name(f, audio_id)
                        else:
                            name = read_name(f)

                        print(f" -- {name}")
                    else:
                        print()

                case 0xC5CCCB70:
                    stream_id = struct.unpack_from(">I", f.read(0x4))[0]
                    flags = struct.unpack_from("<I", f.read(0x4))[0]
                    stream_count = struct.unpack_from("<I", f.read(0x4))[0]
                    header_offset_offset = struct.unpack_from("<I", f.read(0x4))[0]
                    name_offset = struct.unpack_from("<I", f.read(0x4))[0]

                    f.seek(pos + header_offset_offset, 0)
                    header_offset = struct.unpack_from("<I", f.read(0x4))[0] + pos

                    print(f"{count} at 0x{pos:X} -- type 0x{type:X} size 0x{size:X} stream_id 0x{stream_id:X} flags 0x{flags:X} stream_count {stream_count} header_offset 0x{header_offset:X}", end="")

                    if name_offset:
                        name_offset += pos
                        f.seek(name_offset, 0)

                        if flags & 0x8:
                            name = decrypt_name(f, audio_id)
                        else:
                            name = read_name(f)

                        print(f" -- {name}", end="")
                    print()

                    sub_pos = header_offset
                    sub_count = 0
                    while sub_pos < pos + size:
                        f.seek(sub_pos, 0)

                        sub_type = struct.unpack_from(">I", f.read(0x4))[0]
                        sub_size = struct.unpack_from("<I", f.read(0x4))[0]

                        match sub_type:
                            case 0x6AD86FE9 | 0x6FCAB62E | 0x10250527:
                                stream_sub_id = struct.unpack_from(">I", f.read(0x4))[0]
                                num_channels = struct.unpack_from("<I", f.read(0x4))[0]
                                fmt, bps, *_ = struct.unpack_from("<4B", f.read(0x4))
                                sample_rate, num_samples, unk1C = struct.unpack_from("<3I", f.read(3 * 4))
                                loop_start, channel_layout = struct.unpack_from("<iI", f.read(2 * 4))
                                config_offset, config_size = struct.unpack_from("<2I", f.read(0x8))
                                channel_data_offsets_offset, channel_data_sizes_offset = struct.unpack_from("<2I", f.read(0x8))

                                f.seek(sub_pos + config_offset, 0)
                                config = f.read(config_size)

                                f.seek(sub_pos + channel_data_offsets_offset, 0)
                                channel_data_offsets = struct.unpack_from(f"<{num_channels}I", f.read(num_channels * 4))

                                f.seek(sub_pos + channel_data_sizes_offset, 0)
                                channel_data_sizes = struct.unpack_from(f"<{num_channels}I", f.read(num_channels * 4))

                                print(f"\t{sub_count} at 0x{sub_pos:X} -- type 0x{sub_type:X} size 0x{sub_size:X} stream_sub_id 0x{stream_sub_id:X} num_channels 0x{num_channels:X} fmt 0x{fmt:X} bps 0x{bps:X} sample_rate {sample_rate} num_samples 0x{num_samples:X} unk1C 0x{unk1C:X} loop_start {loop_start} channel_layout {channel_layout} config {config}")
                                
                                for i, (channel_offset, channel_size) in enumerate(zip(channel_data_offsets, channel_data_sizes)):
                                    channel_offset += sub_pos
                                    print(f"\t\t{i}: channel_offset 0x{channel_offset:X} channel_size 0x{channel_size:X}")

                                    if EXTRACT_FILES:
                                        f.seek(channel_offset, 0)
                                        channel_data = f.read(channel_size)

                                        out_path = Path(str(file.with_suffix("")) + "_out")
                                        out_path.mkdir(parents=True, exist_ok=True)
                                        (out_path / f"{count}_{name}_ch{i}").write_bytes(channel_data)


                            case 0xA0F4FC6C | 0x793A1FD7:
                                stream_sub_id = struct.unpack_from(">I", f.read(0x4))[0]
                                num_channels = struct.unpack_from("<I", f.read(0x4))[0]
                                unk10 = struct.unpack_from("<I", f.read(0x4))[0]
                                fmt, bps, *_ = struct.unpack_from("<4B", f.read(0x4))
                                sample_rate, num_samples = struct.unpack_from("<2I", f.read(2 * 4))
                                unk20, loop_start, channel_layout, unk2C, unk30 = struct.unpack_from("<IiIII", f.read(5 * 4))
                                data_offset, data_size = struct.unpack_from("<2I", f.read(0x8))
                                unk3C = struct.unpack_from("<I", f.read(0x4))[0]

                                print(f"\t{sub_count} at 0x{sub_pos:X} -- type 0x{sub_type:X} size 0x{sub_size:X} stream_sub_id 0x{stream_sub_id:X} num_channels 0x{num_channels:X} unk10 0x{unk10:X} fmt 0x{fmt:X} bps 0x{bps:X} sample_rate {sample_rate} num_samples 0x{num_samples:X} unk20 0x{unk20:X} loop_start {loop_start} channel_layout {channel_layout} unk2C 0x{unk2C:X} unk30 0x{unk30:X} unk3C 0x{unk3C:X} data_offset 0x{data_offset:X} data_size 0x{data_size:X}")

                                if stream_id in ENCRYPTED_STREAMS:
                                    stream_data = ENCRYPTED_STREAMS[stream_id]
                                    print(f"\t\tFound in ENCRYPTED {stream_data}")

                                    if EXTRACT_FILES:
                                        with open(stream_data["file"], "rb") as stream_file:
                                            stream_file.seek(stream_data["base_pos"] + data_offset, 0)

                                            decrypt_aligned_size = data_size
                                            while decrypt_aligned_size % 0x10:
                                                decrypt_aligned_size += 1
                                            audio_data = stream_file.read(decrypt_aligned_size)

                                        bf = Blowfish.new(stream_data["key"], Blowfish.MODE_ECB)
                                        audio_data = bf.decrypt(audio_data)[:data_size]

                                        decrypt_out_path = Path(str(file.with_suffix("")) + "_out")
                                        #print(decrypt_out_path / f"{count}_{stream_id:x}.KA1A")
                                        decrypt_out_path.mkdir(parents=True, exist_ok=True)
                                        (decrypt_out_path / f"{count}_{name}.ka1a").write_bytes(audio_data)

                                else:
                                    print(f"\t\tNot found in ENCRYPTED")
                                    pass

                            case _:
                                print(f"Unknown subtype 0x{sub_type:X} at 0x{sub_pos:X}")
                                exit()

                        sub_count += 1
                        sub_pos += sub_size
                        while sub_pos % 0x10:
                            sub_pos += 1

                case 0x836FBECA:
                    id = struct.unpack_from(">I", f.read(0x4))[0]
                    flags = struct.unpack_from("<I", f.read(0x4))[0]
                    unk10 = struct.unpack_from("<I", f.read(0x4))[0]
                    unk14 = struct.unpack_from(">I", f.read(0x4))[0]
                    unk18, num_entries = struct.unpack_from("<2I", f.read(0x8))
                    unk20, name_offset, entries_offset = struct.unpack_from("<3I", f.read(3 * 4)) 
                    unk2C = struct.unpack_from(">I", f.read(0x4))[0] 
                    unk30 = struct.unpack_from("<I", f.read(0x4))[0]

                    print(f"{count} at 0x{pos:X} -- type 0x{type:X} size 0x{size:X} id 0x{id:X} flags 0x{flags:X} unk14 0x{unk14:X} unk18 0x{unk18:X} num_entries 0x{num_entries:X} unk20 0x{unk20:X} unk2C 0x{unk2C:X} unk30 0x{unk30:X}")

                    if name_offset:
                        name_offset += pos
                        f.seek(name_offset, 0)

                        name = decrypt_name(f, audio_id)

                        print(f"\t{name}")
                    else:
                        print(f"\tEmpty name")

                    if not flags & 0x10000:
                        f.seek(pos + entries_offset, 0)
                        entries = struct.unpack_from(f"<{num_entries}I", f.read(num_entries * 0x4))
                        for i,entry in enumerate(entries):
                            f.seek(pos + entry, 0)

                            sub_name = decrypt_name(f, audio_id)

                            print(f"\t\t{sub_name}")

                case 0x2D232C98:
                    id = struct.unpack_from(">I", f.read(0x4))[0]
                    unk0C = struct.unpack_from("<I", f.read(0x4))[0]
                    unk10 = struct.unpack_from(">I", f.read(0x4))[0]
                    unk14 = struct.unpack_from("<I", f.read(0x4))[0]
                    unk18 = struct.unpack_from("<I", f.read(0x4))[0]
                    unk1C = struct.unpack_from("<f", f.read(0x4))[0]
                    unk20 = struct.unpack_from("<I", f.read(0x4))[0]
                    num_entries = struct.unpack_from("<I", f.read(0x4))[0]
                    entries_offsets_offset = struct.unpack_from("<I", f.read(0x4))[0]
                    unk2C = struct.unpack_from("<I", f.read(0x4))[0]
                    unk30 = struct.unpack_from("<I", f.read(0x4))[0]
                    name_offset = struct.unpack_from("<I", f.read(0x4))[0]

                    f.seek(pos + entries_offsets_offset, 0)
                    entries_offsets = struct.unpack_from(f"<{num_entries}I", f.read(num_entries * 0x4))

                    if name_offset:
                        f.seek(pos + name_offset, 0)

                        name = decrypt_name(f, audio_id)

                        print(f"\t{name}")
                    else:
                        print(f"\tEmpty name")

                    for i,entry in enumerate(entries_offsets):
                        entry_base = pos + entry
                        f.seek(entry_base, 0)

                        f.seek(entry_base + 0x30, 0)
                        name_offset = struct.unpack_from("<I", f.read(0x4))[0]

                        if name_offset:
                            f.seek(entry_base + name_offset, 0)

                            name = decrypt_name(f, audio_id)

                            print(f"\t\t{i}: {name}")
                        else:
                            print(f"\t\t{i}: Empty name")

                case _:
                    print(f"Unknown type 0x{type:X} at 0x{pos:X}")
                    exit()

            pos += size

            count += 1

