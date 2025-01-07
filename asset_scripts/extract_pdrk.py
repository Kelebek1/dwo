from pathlib import Path
import struct
import sys
import zlib
import concurrent.futures

def set_output_suffix(path, magic):
    valid = False
    for c in magic:
        if c < 0x20 or c >= 0x7F:
            break;
    else:
        magic = magic.decode("utf8")
        valid = True

    if valid:
        return path.with_suffix(f".{magic.lower()}")
    return path

def read_file(out_file_path, in_file_name):
    out_file_path = out_file_path / f"{in_file_name.stem}"
    out_file_path.mkdir(parents=True, exist_ok=True)

    print(f"Processing file {in_file_name.stem}")

    in_file_size = in_file_name.stat().st_size

    with open(in_file_name, "rb") as f:
        f.seek(0, 0)
        magic, pdrk_header_size, pdrk_size = struct.unpack_from("<8sII", f.read(0x10))

        assert magic[:4] == b"PDRK", f"Expected magic to be PDRK"

        if pdrk_size == 0:
            exit()

        pos = pdrk_header_size
        num_files = 0

        while pos < in_file_size:
            f.seek(pos, 0)

            base_pos = pos

            magic, idrk_size, comp_size, decomp_size, \
            unk20, file_hash, unk28_hash, unk2C, \
            unk30_hash, unk34 = struct.unpack_from("<8sQQQIIIIII", f.read(0x38))

            assert magic[:4] == b"IDRK", f"Expected magic to be IDRK but got {magic} at 0x{pos:X}"
            
            print(f"\tReading file {file_hash:x} from 0x{pos:X}")

            pos += 0x38

            if unk20 == 1 and unk34 == 1:
                pos += 0xD
            else:    
                pos += unk34 * 0x10


            data = bytes()

            end = base_pos + idrk_size
            while pos < end:
                f.seek(pos, 0)

                size = struct.unpack_from("<H", f.read(2))[0]

                if size == 0:
                    break;

                pos += 0xA
                f.seek(pos, 0)

                data += zlib.decompress(f.read(size))

                pos += size

            assert len(data) == decomp_size, f"Expected decompressed size 0x{decomp_size:X} but only got 0x{len(data):X}"

            pos = end

            #print(f"Ending file read at 0x{pos:X}")
            while pos % 0x10:
                pos += 1

            path = out_file_path / f"{num_files}_{file_hash:x}"
            path = set_output_suffix(path, data[:4])
            path.write_bytes(data)

            #exit()

            num_files += 1

        #print(f"{num_files} read")

def rename(in_path):
    #out_file_path = out_file_path / in_file_name.stem

    for file_path in Path.glob(in_path, f"**/*"):
        if not file_path.is_file():
            continue
        if file_path.suffix:
            continue
        if file_path.stat().st_size < 4:
            continue

        valid = False
        with open(file_path, "rb") as f:
            magic = struct.unpack_from("4s", f.read(4))[0]
            for c in magic:
                if c < 0x20 or c >= 0x7F:
                    break;
            else:
                magic = magic.decode("utf8")
                valid = True
                #print(f"{file_path} = {magic}")

        if valid:
            #print(f"{file_path} into {file_path.with_suffix(f".{magic}")}")
            try:
                file_path.rename(file_path.with_suffix(f".{magic}"))
            except Exception:
                continue

if __name__ == '__main__':
    in_path = Path(sys.argv[1])

    if not in_path.is_file():
        files = [f for f in in_path.glob("*.fdata")]
        out_path = in_path / "extracted"
    else:
        files = [in_path]
        out_path = in_path.parent / "extracted"

    Path.mkdir(out_path, parents=True, exist_ok=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for file in files:
            executor.submit(read_file, out_path, file)
