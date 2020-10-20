# Write a function that extracts the words from a given text
# as a parameter. A word is defined as a sequence of
# alpha-numeric characters.

import re


def listOfWords(text):
    # returns list of words in text

    # both do the same
    # re.split("\W+", text)

    return re.findall(r"(\w+)", text)


print(listOfWords("Erase una vez"))
