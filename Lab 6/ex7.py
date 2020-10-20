# Verify using a regular expression whether a string is a valid CNP

import re


def validDNI(dni):
    return re.match("^[0-9]{8}[a-zA-Z]$", dni)  # ^ for being in the begining, $ for being in the end


DNI = raw_input("Write your DNI: ")

if validDNI(DNI):
    print("Valid")
else:
    print("Not valid")
