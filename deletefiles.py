import os
import time
folderpath = "/Users/kavyasibbala/Documents/tmp"
days_old = 3
now = time.time()

for file in os.listdir(folderpath):
    file_path = os.path.join(folderpath, file)
    if os.path.isfile(file_path):
        file_age = now - os.path.getmtime(file_path)
        if file_age > days_old*86400:
            os.remove(file_path)
            print(f"{file} deleted")
    else:
        print(f"Its a directory-skipping")