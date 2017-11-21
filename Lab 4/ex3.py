# Write a function that receives a filename as a parameter and writes
# the data from the os.environ in the file, each line containing an
# entry in this dictionary, in the form of the key [tab] value.

import os
#import pdb; pdb.set_trace()

filename = raw_input("Enter the name of a file: ")

try:
	fd = open(filename, mode = 'w')
except IOError:
	print "Could not open file"

for a in os.environ:
	entry = a + "\t" + os.environ[a] + "\n"

	try:
		fd.write(entry)
	except IOError:
		print "Could not write in the file"

fd.close()