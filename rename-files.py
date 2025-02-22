import os
folderpath = "/Users/kavyasibbala/Documents/tmp"
files = os.listdir(folderpath)
for file in files:
    oldfile = os.path.join(folderpath, file)
    if not file.endswith("_backup.txt"):
        # Create new name by removing the file extension and adding '_backup'
        name, ext = os.path.splitext(file)
        newfile = os.path.join(folderpath, f"{name}_backup{ext}")
        os.rename(oldfile, newfile)
        print(f"Renamed: {file} → {name}_backup{ext}")
    else:
        print(f"Skipped: {file} (already has '_backup.txt')")
