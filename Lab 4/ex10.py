# -*- coding: utf-8 -*-

# Write a search_by_content function that receives two target string and to_search as
# a parameter and returns a list of files containing to_search. The files are searched
# as follows: if the target is a file, it is searched only in that file and if it is
# a directory it will search recursively for all the files in that directory. If the
# target is neither a file nor a directory, it will drop a ValueError exception with 
# an appropriate message.

import os, sys
# import pdb; pdb.set_trace()

# Colors for displaying the answers
GREEN = '\033[32m'
BLUE = '\033[34m'
RED = '\033[31m'
RESET = '\033[0m'

def search_by_content(path, to_search):
	if not os.path.isdir(path):
		print RED + path, "is not a directory" + RESET
		sys.exit()

	for root, directories, filenames in os.walk(path):
		for filename in filenames:
			try:
				fd = open(os.path.join(root, filename), mode = "r")
			except:
				print RED + "Couldn't open", os.path.join(root, filename) + RESET
				sys.exit()
			
			if to_search in fd.read():
				print os.path.join(root, filename)


print search_by_content("/Users/jesusjimsa/Dropbox/Documentos/Universidad/3 - Primer cuatrimestre/Python Programming/Prácticas", "def")