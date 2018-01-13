# Write two scripts that communicate each other through serialized data.
# The first script will periodically save a list of all the files in a directory,
# and the second script will add in an archive all the files smaller than 100kb
# modified at most 5 minutes ago (the same file will not be added twice).

import sys
import os
import json
import time

in_file = "saved.data"
out_file = "saved_small.data"
wait_period = 10
maxSize = 100 * 1000
maxTime = 5 * 60

while True:
	the_list = list()
	start_time = time.time()
	
	js = json.load(open(in_file, 'r'))

	for file in js:
		file_path = os.path.abspath(file)

		if os.path.getsize(file_path) < maxSize:
			if (start_time - os.path.getmtime(file_path)) < maxTime:
				the_list.append(file)
		
	fd = open(out_file, 'w')
	json.dump(the_list, fd, indent = 4)
	fd.close()

	print "Data saved, let's sleep"
	time.sleep(wait_period)