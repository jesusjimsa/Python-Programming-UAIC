# Write a function that returns the number of words
# that exist in a string. Words are separated by
# spaces, punctuation marks (, ;, ? ! . )

def wordCounter(cadena):
	count = 1
	punctuation = [" ", ",", ";", "?", "!", "."]

	for i in cadena:
		if i in punctuation:
			count += 1

	if cadena[len(cadena) - 1] in punctuation:
		count -= 1

	return count

print "Hay", wordCounter("Hola me llamo Jesus."), "palabras en la frase Hola, me llamo Jesus"