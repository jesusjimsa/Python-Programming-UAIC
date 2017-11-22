# -*- coding: utf-8 -*-
 
# Write a get_file_info function that receives as a parameter a string representing
# the path to a file and returns a dictionary with the following fields:
# full_path = # absolute path to the file
# file_size = # file size in bytes
# file_extension = # file extension (if it has) or ""
# can_read = True / False # if you can read from file
# can_write = True / False # if you can write to file
 
import sys, os
 
# Colors for displaying the answers
GREEN = '\033[32m'
BLUE = '\033[34m'
RED = '\033[31m'
RESET = '\033[0m'
 
def get_file_info(path):
    if not os.path.isfile(path):
        print RED + path, "is not a file" + RESET
        sys.exit()
     
    info = dict()
 
    info["full_path"] = os.path.realpath(path)
    info["file_size"] = os.path.getsize(path)
    filename, file_extension = os.path.splitext(path)
    info["file_extension"] = file_extension
 
    try:
        fdR = open(path, mode = "r")
    except:
        info["can_read"] = "False"
    else:
        info["can_read"] = "True"
        fdR.close()
     
    try:
        fdW = open(path, mode = "w")
    except:
        info["can_write"] = "False"
    else:
        info["can_write"] = "True"
        fdW.close()
 
    return info
 
res = get_file_info("ex11.py")
 
for a in res:
    print a, "=", res[a]
	