# TODO: idk its not working
# TODO: maybe delete the junk files before moving to a folder ath begining
# TODO: copy and paste this code into both gpt and copilot
import string
from ctypes import windll
import os
import sys
import json
import shutil

LOCATION = " ".join(sys.argv[1].split(","))[2:-6].split(" ")
junks = ['dat', 'ses', 'tmp', 'log', 'db-shm']

def delete(loc):
    # Extract the file extension
    file_extension = loc.split("/")[-1].split("'")[0]
    print(file_extension)
    
    # Check if the file extension is in the junks list
    if file_extension in junks:
        # Use os.remove() to delete the file
        shutil.rmtree(loc)
        print("loool")

for i in LOCATION:
    if i:
        print(i.split("/")[-1].split("'")[0])
        delete(i)
