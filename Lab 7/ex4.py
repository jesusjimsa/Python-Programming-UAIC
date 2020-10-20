# -*- coding: utf-8 -*-
# Write a script that receives a directory as argument and creates a JSON file with
# data about all the files in that directory. For each file, the following
# information will be displayed: file_name, md5_file, sha256_file, size_file (in
# bytes), time when the file was created (human-readable) and the absolute path to
# the file.

import time
import sys
import os
import json
import hashlib


def filesToJson(directory):
    entries = os.listdir(directory)

    for entry in entries:
        if os.path.isfile(entry):
            file_name = entry
            md5_file = hashlib.md5(entry).hexdigest()
            sha256_file = hashlib.sha256(entry).hexdigest()
            size_file = os.path.getsize(entry)
            creation = time.ctime(os.path.getctime(entry))
            absolute = os.path.abspath(entry)

            d = {
                "file_name": file_name,
                "md5_file": md5_file,
                "sha256_file": sha256_file,
                "size_file": size_file,
                "creation": creation,
                "absolute": absolute
                }

            s = json.dumps(d, indent=4)
            open("file_info.json", "wt").write(s)


filesToJson("/Users/jesusjimsa/Dropbox/Documentos/Universidad/3 -" +
            "Primer cuatrimestre/Python Programming/Prácticas/Lab 1")
