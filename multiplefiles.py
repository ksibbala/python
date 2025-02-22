import os
folderpath = "/Users/kavyasibbala/Documents/tmp"
num_files = 3
for num in range(num_files):
    filepath = os.path.join(folderpath, f"file{num}")
    with open(filepath, 'w') as f:
        f.write(f"This is the content of file{num}.")
    print(f"file{num} is created")