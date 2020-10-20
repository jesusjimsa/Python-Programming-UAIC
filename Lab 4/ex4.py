# -*- coding: utf-8 -*-

# Write a function that receives as a parameter a path that
# represents a directory on the system, recursively browses
# the file structure and directories that it contains and
# displays in the console all the paths it has traveled.
# You are NOT allowed to use os.walk.

import os
import sys


def recursive(directory, tabs=""):
    try:
        entries = os.listdir(directory)
    except OSError:
        print(directory, "is not a directory")
        sys.exit()

    for element in entries:
        FilDir = os.path.join(directory, element)
        print(tabs, FilDir)

        if os.path.isdir(FilDir):
            tabs += "\t"
            recursive(FilDir, tabs)
            tabs = tabs[0:len(tabs) - 1]    # Delete the last tab


print(recursive("/Users/jesusjimsa/Dropbox/Documentos/Universidad/3 - Primer cuatrimestre/Python Programming/Prácticas"))
print(recursive("/Users/jesusjimsa/Dropbox/Capturas de pantalla/Captura de pantalla 2017-05-16 12.00.17.png"))
