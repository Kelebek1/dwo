The scripts here are for the `File/ASSET/FDataPackage/Dev` folder, mainly for extracting audio.

Use `extract_pdrk.py` to extract the `*.fdata` files. Accepts a file or folder path as input.

Use `parse_ktsr.py` to extract the `.asrs` files, or for the `.file` files in the `data/` folders. Accepts a file or folder path as input.
    All of the `data/` folders only contain audio, and the audio is referenced from the ASRS files. 
    `parse_ktsr.py` will print a bunch of information from the ASRS files about the sounds, and extract what it can. Sounds which have the 0x10000 flag are "external", which means their data will be in one of the `data/` archives. Otherwise they have internal data inside the ASRS.
    The internal type of sounds aren't extracted at all yet.

Use `ka1a_decoder` to decode the `.ka1a` files which are produced by `parse_ktsr.py`. Also can take a single file or folder path as input.
    This project is a mess and isn't finished, it was only made to test decoding so it's not great. Functions are pulled straight from IDA and just made compilable, with a bunch of bug fixes just to make it work.
    It produces audio streams which are all raw 48Khz (checkable in the .ka1a header, so may change, but everything I've seen is 48Khz) float (f32) data. The number of channels is variable so it's included in the filename. Audacity can import this as Raw Data and play it just fine. You'll want to import all streams from the same file if there are multiple, like for bgm000 and bgm001.
    Don't have an automated way of decoding asrs files directly to the output float (or other format cause it's massive) files yet.

0x1dde41d9 in the main Dev folder has most of the non-language-specific audio, like movie background sound and BGMs.
enUS/0x5fe6b213 has all of the voice audio.
