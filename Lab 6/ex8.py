# Write a function that recursively scrolls a directory and displays those
# files whose name matches a regular expression given as a parameter or
# contains a string that matches the same expression. Files that satisfy
# both conditions will be prefixed with ">>"

import os
import re


def fileMatches(directory, regex):
    for _, directories, filenames in os.walk(directory):
        for directory in directories:
            print(directory)
        for filename in filenames:
            if re.match(regex, filename):
                print(">>" + filename)
            else:
                print(filename)


fileMatches("/Users/jesusjimsa/Dropbox/Documentos/Universidad", r"[a-zA-Z]*\d[a-zA-Z]*")
