import struct
from pathlib import Path
import chars

FILES = {
    17: {"entry_size":0x14, "text_offset":0x0, "speaker_offset":0xC},
    30: {"entry_size":0x8, "text_offset":0x0},
    31: {"entry_size":0x4, "text_offset":0x0},
    32: {"entry_size":0x4, "text_offset":0x0},
}
string_path = Path.cwd().parent.parent.parent / "LANG" / "ENG" / "LINKDATA_LANG_ENG"
if not string_path.exists():
    print(f"Could not find path to strings \"{string_path}\"\nHave you extracted the language-specific LINKDATA inside \"LinkData/LANG/ENG\"?")
    exit()

def get_string(file_idx, string_idx):
    if file_idx not in FILES:
        print(f"Unknown string file {file_idx}")
        exit()

    with open(string_path / f"{file_idx}", "rb") as f:
        fd = f.read()

    num_strings = struct.unpack_from("<I", fd, 0)[0]

    if string_idx >= num_strings:
        print(f"Invalid string index, file only has {num_strings} but idx given was {string_idx}")
        exit()

    entry_pos = 0x10 + string_idx * FILES[file_idx]["entry_size"]
    string_offset_pos = entry_pos + FILES[file_idx]["text_offset"]
    string_offset = struct.unpack_from("<I", fd, string_offset_pos)[0]

    if file_idx == 17:
        speaker_id = struct.unpack_from("<I", fd, entry_pos + FILES[file_idx]["speaker_offset"])[0]
        speaker = chars.char_id_to_name(speaker_id)

        string = f"{speaker}: " + fd[string_offset_pos + string_offset : fd.find(b"\x00", string_offset_pos + string_offset)].decode("utf8")
    else:
        string = fd[string_offset_pos + string_offset : fd.find(b"\x00", string_offset_pos + string_offset)].decode("utf8")

    return string
    
def get_index(file_idx, string):
    if file_idx not in FILES:
        print(f"Unknown stirng file {file_idx}")
        exit()

    with open(string_path / f"{file_idx}", "rb") as f:
        fd = f.read()

    num_strings = struct.unpack_from("<I", fd, 0)[0]

    for idx in range(num_strings):
        entry_pos = 0x10 + idx * FILES[file_idx]["entry_size"]
        string_offset_pos = entry_pos + FILES[file_idx]["text_offset"]
        string_offset = struct.unpack_from("<I", fd, string_offset_pos)[0]

        cmp_string = fd[string_offset_pos + string_offset : fd.find(b"\x00", string_offset_pos + string_offset)].decode("utf8")

        if cmp_string == string:
            return idx

    print(f"Invalid string {string} for file {file_idx}")
    exit()
