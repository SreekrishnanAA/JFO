import string
from ctypes import windll
import shutil
import os
import sys

LOCATION = sys.argv[1]

TOTAL_FILES = 0
TOTAL_SIZE = 0
ORGANIZED_FILES = 0
DELETED_FILES = 0

# TODO: 1st step
def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives

def list_folders(directory_path):
    files_and_folders = os.listdir(directory_path)
    folders = [item for item in files_and_folders if os.path.isdir(os.path.join(directory_path, item))]
    folders.sort()
    return folders

junks = ['dat', 'ses', 'tmp', 'log', 'db-shm']
dic = {}
for i in os.listdir(LOCATION):
    TOTAL_FILES += 1
    try:
        if i.split(".")[-1] not in dic and i.split(".")[-1] not in junks:
            dic[i.split(".")[-1]] = 1
        else:
            dic[i.split(".")[-1]] += 1
    except Exception as e:
        # print(f"Error processing file {i}: {e}")
        pass



# TODO - real implementation
args = []

for i in dic.keys():
    dir_path = LOCATION + "/" + i
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        args.append(dir_path)

for i in os.listdir(LOCATION):
    if "." not in i:
        continue

    ext = i.split(".")[-1]

    if ext in junks:
        os.remove(LOCATION + "/" + str(i))

    source_path = LOCATION + "/" + str(i)
    destination_path = LOCATION + "/" + ext + "/" + str(i)
    if source_path != destination_path:
        try:
            shutil.move(source_path, destination_path)
        except FileNotFoundError:
            pass
        except NotADirectoryError:
            pass
        except PermissionError:
            pass
        
def count_rem(loc):
    total = 0
    for root, dirs, files in os.walk(loc):
        total += len(files)
    return total

def count_size(loc):
    total = 0
    for root, dirs, files in os.walk(loc):
        for f in files:
            fp = os.path.join(root, f)
            total += os.path.getsize(fp)
    return total

TOTAL_SIZE = count_size(LOCATION)
# TOTAL_SIZE = round(TOTAL_SIZE, 2)
ORGANIZED_FILES = count_rem(LOCATION)
DELETED_FILES = TOTAL_FILES - ORGANIZED_FILES
print(str(TOTAL_FILES) + ":" + str(DELETED_FILES), ":" + str(ORGANIZED_FILES) + ":" + str(TOTAL_SIZE))
