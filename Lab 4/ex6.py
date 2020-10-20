# Write a script that receives 3 parameters from the console. The first one
# will be a path to a file, the second a path to a directory and the third
# will be the size of a buffer. Script will copy the given file as a
# parameter into the given directory as a parameter, using a buffer of the
# third parameter size, in bytes.

import sys
import os


fileName = raw_input("Write the path to the file: ")
directory = raw_input("Write the path to the directory: ")
num_bytes = int(raw_input("Write the size of the buffer: "))

try:
    fd = open(fileName, mode='r')
except IOError:
    print("Couldn't open", fileName)
    sys.exit()

try:
    os.path.isdir(directory)
except OSError:
    print(directory, "is not a directory")
    sys.exit()

newFile = directory + "/newFile.txt"

try:
    new_fd = open(newFile, mode='w')
except IOError:
    print("Couldn't create new file")
    sys.exit()

try:
    new_fd.write(fd.read(num_bytes))
except IOError:
    print("Couldn't write in the new file")
    sys.exit()

fd.close()
new_fd.close()
