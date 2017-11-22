# Write a function that receives as a parameter a regex string, a text string and
# a whole number x, and returns those long-length x substrings that match the
# regular expression.

import re

#import pdb; pdb.set_trace()

def regex_text_number(regex, text, number):
	expression = regex + "{" + str(number) + "}"
	return re.findall(expression, text)

print regex_text_number("\d", "Hola, tengo 3 anios y 5389 cabras", 4)