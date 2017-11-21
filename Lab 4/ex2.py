# Write a script which takes as parameter from the command line
# a path and displays the first 4096 bytes if the path leads to
# a file, it's entries if the path is a directory and an error
# message if the path is not a valid one.

import os
#import pdb; pdb.set_trace()

pathFD = raw_input("Write a path: ")

if os.path.isdir(pathFD):
	print os.listdir(pathFD)
elif os.path.isfile(pathFD):
	try:
		fd = open(pathFD, mode = 'r')
	except IOError:
		print "Could not open file"
		sys.exit()
	try:
		print fd.read(4096)
	except IOError:
		print "Could not read file"
		sys.exit()
else:
	print "The path is not valid"