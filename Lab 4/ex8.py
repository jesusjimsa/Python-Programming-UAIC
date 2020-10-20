# Write a script that takes the following arguments: path, tree_depth, filesize,
# filecount, dircount and create a directory structure deep depth as follows:
# starting from the root path will be created dircount filecount directories and
# files containing filesize bytes (only the "a" character for example) and this
# process will be repeated recursively for each created directory until the desired
# depth is reached (in directories at the maximum depth, no other directories will
# be created)

import os
import sys


path = raw_input("Write the root path: ")

if not os.path.isdir(path):
    print(path, "is not a directory")
    sys.exit()

tree_depth = int(raw_input("Write the maximum depth: "))
filesize = int(raw_input("Write the file size: "))
filecount = int(raw_input("Write the number of files: "))
dircount = int(raw_input("Write the number of directories: "))

if tree_depth < 0 or filesize < 0 or filecount < 0 or dircount < 0:
    print("None of the numbers can be negative")
    sys.exit()

for root, directories, filenames in os.walk(path):
    filebegin = 0
    dirbegin = 0

    for directory in directories:
        if dirbegin < dircount:
            print(os.path.join(root, directory))
            dirbegin += 1

        depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
        if depth == tree_depth:
            directories[:] = []     # Don't recurse any deeper
    for filename in filenames:
        if os.path.getsize(os.path.join(root, filename)) == filesize:
            print(os.path.join(root, filename), "(", os.path.getsize(os.path.join(root, filename)), ")")

            if filebegin < filecount:
                filebegin += 1

        depth = root[len(path) + len(os.path.sep):].count(os.path.sep)
        if depth == tree_depth:
            filenames[:] = []   # Don't recurse any deeper
