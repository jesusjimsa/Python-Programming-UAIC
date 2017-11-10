# Write a function that receives a string as a parameter
# and returns a dictionary in which the keys are the
# characters in the character string and the values are 
# he number of occurrences of that character in the given
# text.
#
# Example: For string "Ana has apples." given as a
# parameter the function will return the dictionary:
# {'A': 1, '': 2, 'n': 1, 'a': 2, 'p': 2, '.': 1}.

def characterCounter(cadena):
	counter = dict()

	for i in range(0, len(cadena)):
		if cadena[i] in counter:
			counter[cadena[i]] += 1
		else:
			counter[cadena[i]] = 1

	return counter

print characterCounter("Ana has apples.")