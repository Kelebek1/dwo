The scripts here are for de/recompiling stage scripts, and are intended to be placed in `LinkData/CMN/EX/TRIAL` and run from there.

1. Use `extract.py <filepath>` to extract `LinkData/CMN/LINKDATA_A.BIN` and `LinkData/LANG/ENG/LINKDATA_LANG_ENG.BIN`.

2. Use `decompile_script.py <stage index>` with an index in the range 1194 - 1834, or "orig", to decompile that stage index as extracted from LINKDATA_A into `<stage_index>_units.yaml` and `<stage_index>_script.yaml`.
    "orig" is for the demo stage script which is the only one in LINKDATA_EX_TRIAL.BIN, as opposed to the "real" stages for the game in LINKDATA_A.
    Note that as of the demo patch 1.01 a lot of things were removed, which unfortunately included the stage scripts. Now, every stage script 1194 - 1834 in LINKDATA_A was replaced with a copy of the demo script, so they're all identical. If you get an original version of LINKDATA_A you can decompile all the stage scripts, but if you're on the patch you may as well just use "orig" as there's nothing different with any other file.

3. Modify `x_units.yaml` and `x_script.yaml` as you like. Using invalid values will likely crash the game, such as trying to spawn units not included in the demo, as their files just don't exist so the game dies trying to load them. You can remove entire scripts, remove their conditions, remove individual opcodes etc etc and then try to see what happens differently in the game to figure out what opcode is what.

4. Use `compile_script.py <stage index>` to recompile the script. This will replace the demo stage script in `LINKDATA_EX_TRIAL.BIN`, but the scripts should have made a .orig backup so you don't lose the original. You can always get it back from Steam if you lose it anyways.

If you want to modify the output, like adding opcode names and stuff to the output, you'll need to modify `opcodes_conditions.py` or `opcodes_script.py` which contain the definitions for all the opcodes, with each one having a compile and decompile function.

You'll need to modify `OPCODES_X` at the top for changing argument names, and also change the code in the compile/decompile functions, and you can rename the class, which also means you need to modify `HANDLERS_X` at the bottom as well.


By default `script_compiled` will be saved each time you compile, which is the compiled version of the script before it's encrypted and added into the LINKDATA archive. You can explore this file and mess with other parts of it too if you want, as I don't know much about it.

There are 15 tables in the stage files, the first dword in the file is the table count. Following the table count are the offset and size in dwords for each table, so table 0 is always at 0x7C. 4 + 15 * 8 = 0x7C

Counting from 0, table 1 (at 0x124 in the demo stage) contains the unit definitions, and the last one, table 14 (at 0xA410 in the demo stage), contains the game script which makes up most of the file. These 2 are decompiled, but I don't know what any of the other tables are. Let me know if you find out. Table 0 contains at least the message indexes for the victory/defeat conditions shown on the prep menu.
