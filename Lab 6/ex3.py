# Write a function that receives as a parameter a string of text
# characters and a list of regular expressions and returns a list
# of strings that match on at least one regular expression given
# as a parameter.

import re


def listOfExpressions(characters, expressionsList):
    solutions = dict()

    for a in expressionsList:
        solutions[a] = re.findall(a, characters)

    return solutions


chars = "ertyui 1 oknb 5 vcxpv 6 cdsrtyui 3 kbvd"
expressions = [r"\d", r"\w+"]

print(listOfExpressions(chars, expressions))
