# Write a script that receives 2 parameters from the console representing
# a path to a directory on the system and a file name. The script will
# recursively navigate to the file structure and directories in the given
# directory as a parameter using os.walk and write in the file given as a
# parameter all sites path you travelled and it's type
# (FILE, DIRECTORY, UNKNOWN), separated by |.
# Each path will be written on one line.

import os
import sys

directory = raw_input("Write a path: ")
entries = raw_input("Write the name of the new file: ")

try:
    fd = open(entries, mode='w')
except IOError:
    print("Error creating or openin the file", entries)
    sys.exit()

for root, directories, filenames in os.walk(directory):
    for directory in directories:
        to_write = os.path.join(root, directory) + " | DIRECTORY\n"
        try:
            fd.write(to_write)
        except IOError:
            print("Unable to write in", entries)
            sys.exit()
    for filename in filenames:
        if os.path.isfile(filename):
            to_write = os.path.join(root, filename) + " | FILE\n"
            try:
                fd.write(to_write)
            except IOError:
                print("Unable to write in", entries)
                sys.exit()
        else:
            to_write = os.path.join(root, filename) + " | UNKNOWN\n"
            try:
                fd.write(to_write)
            except IOError:
                print("Unable to write in", entries)
                sys.exit()

fd.close()
