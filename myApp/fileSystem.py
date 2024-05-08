import string
from ctypes import windll
import json
import os
import sys
# os.chdir("C:/Users/admin/junkFileOrganizer/myApp")

FOLDER_AND_DIRS = {}

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives
drives = get_drives()

def list_files_and_folders(directory_path):
    try:
        files_and_folders = os.listdir(directory_path)
    except PermissionError:
        return [], []
    folders = [item for item in files_and_folders if os.path.isdir(os.path.join(directory_path, item))]
    files = [item for item in files_and_folders if os.path.isfile(os.path.join(directory_path, item))]
    folders.sort()
    files.sort()
    return folders, files


# folders, files = list_files_and_folders("D:/")
# print(os.path.isfile("D:/" + folders[0]))

for i in drives:
    folders, files = list_files_and_folders(i + ":/")
    FOLDER_AND_DIRS[i] = {folder: [] for folder in folders}


for i in FOLDER_AND_DIRS.keys():
    for j in FOLDER_AND_DIRS[i]:
        folders, files = list_files_and_folders(i + ":/" + j)
        for k in files:
            temp = {}
            temp["name"] = k
            temp["extension"] = k.split(".")[-1]
            temp["type"] = "File"
            FOLDER_AND_DIRS[i][j].append(temp)
        
        for k in folders:
            temp = {}
            temp["name"] = k
            temp["extension"] = "Folder"
            temp["type"] = "Folder"
            FOLDER_AND_DIRS[i][j].append(temp)
        

# json_data = json.dumps(FOLDER_AND_DIRS, indent=4)
with open('output.json', 'w') as f:
    json.dump(FOLDER_AND_DIRS, f, indent=4)


print("Current working directory:", os.getcwd(), "\n")
print("Current user:", os.getlogin(), "\n")
print("Python executable:", sys.executable, "\n")
