# Find all the duplicate files in a directory given as an argument and display
# the run time. The path of the duplicate file groups will be written to an
# output.txt file.

import os
import sys
import hashlib
import time

def hashfile(path, blocksize = 65536):
	afile = open(path, 'rb')
	hasher = hashlib.md5()
	buf = afile.read(blocksize)

	while len(buf) > 0:
		hasher.update(buf)
		buf = afile.read(blocksize)

	afile.close()

	return hasher.hexdigest()

def findDup(parentFolder):
	# Dups in format {hash:[names]}
	dups = {}

	for dirName, subdirs, fileList in os.walk(parentFolder):
		#print('Scanning %s...' % dirName)

		for filename in fileList:
			# Get the path to the file
			path = os.path.join(dirName, filename)

			# Calculate hash
			file_hash = hashfile(path)

			# Add or append the file path
			if file_hash in dups:
				dups[file_hash].append(path)
			else:
				dups[file_hash] = [path]

	return dups

start_time = time.time()

hola = findDup(sys.argv[1])

print("--- %s seconds ---" % (time.time() - start_time))

fd = open("output.txt", "w")

fd.write("Duplicated files\n")

for a in hola:
	entry = str(hola[a])
	fd.write(entry)
	fd.write("\n")