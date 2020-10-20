# Write two scripts that communicate each other through serialized data.
# The first script will periodically save a list of all the files in a directory,
# and the second script will add in an archive all the files smaller than 100kb
# modified at most 5 minutes ago (the same file will not be added twice).

import sys
import os
import json
import time


if len(sys.argv) != 2:
    print("Expected folder path")
    sys.exit()

folder = sys.argv[1]

out_file = "saved.data"
wait_period = 10

while True:
    the_list = list()

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)

        if os.path.isfile(file_path):
            the_list.append(file_path)

    fp = open(out_file, 'w')
    json.dump(the_list, fp, indent=4)
    fp.close()

    print("Data saved, let's sleep")
    time.sleep(wait_period)
