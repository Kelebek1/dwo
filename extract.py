import struct
import sys
from pathlib import Path
import zlib
import file_crypt

def set_output_suffix(path, magic):
    try:
        magic = magic.decode("utf8")
    except Exception:
        return path

    valid = False
    for c in magic:
        if ord(c) < 0x20 or ord(c) >= 0x7F or c in r"!\#$%&'()*+,-./\"`":
            break;
    else:
        valid = True

    if valid:
        return path.with_suffix(f".{magic.lower()}")
    return path

def decompress(data):
    decomp_size = struct.unpack_from("<I", data, 0)[0]

    out_data = []
    pos = 4
    while pos < len(data):
        comp_size = struct.unpack_from("<I", data, pos)[0]

        if comp_size == 0:
            break;

        out_data.append(zlib.decompress(data[pos + 4:pos + 4 + comp_size]))

        pos += 4 + comp_size

    return b"".join(out_data)

in_path = Path(sys.argv[1])

with open(in_path, "rb") as f:
    magic, file_count, alignment = struct.unpack_from("<III", f.read(0xC))

    pos = 0x10
    for file in range(file_count):
        f.seek(pos, 0)

        offset, comp_size, decomp_size = struct.unpack_from("<QII", f.read(0x10))
        pos += 0x10

        offset *= alignment

        #if comp_size == 0xBB83C:
        #    print(f"{file} -- 0x{pos - 0x10:08X} -- offset 0x{offset:08X} comp_size 0x{comp_size:08X} decomp_size 0x{decomp_size:08X}")
        print(f"{file} -- 0x{pos - 0x10:08X} -- offset 0x{offset:08X} comp_size 0x{comp_size:08X} decomp_size 0x{decomp_size:08X}")
        #continue

        f.seek(offset, 0)

        data = f.read(comp_size)
        data = file_crypt.crypt(data, "dec")

        #with open("test_decrypt.bin", "wb") as f:
        #    f.write(data)

        if decomp_size != 0:
            data = decompress(data)

        out_path = in_path.with_suffix("")
        out_path.mkdir(parents=True, exist_ok=True)
        out_path = out_path / f"{file}"
        if len(data) > 4:
            out_path = set_output_suffix(out_path, data[:4])
        out_path.write_bytes(data)

        #exit()

