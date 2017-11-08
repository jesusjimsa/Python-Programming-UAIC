# Write a function that returns the largest prime
# number from a string given as a parameter or -1
# if the character string contains no prime number.
# Ex: input:
# 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda';
# output: 271

def is_prime(a):
    return all(a % i for i in xrange(2, a))	# Check if a number is prime

def largestPrime(cadena):
	numbersString = list()
	numbers = list()
	maxPrime = -1
	cantidadNumeros = 0
	i = 0

	# Save every number as a string
	while i < len(cadena):
		if cadena[i].isdigit():
			cantidadNumeros += 1

			numbersString.append(cadena[i])

			while cadena[i + 1].isdigit():
				numbersString[cantidadNumeros - 1] += cadena[i + 1]
				i += 1
		
		i += 1
	
	# Convert every string number into an actual number
	for elem in numbersString:
		numbers.append(int(elem))
	
	# Look for the largest prime
	for a in numbers:
		if is_prime(a):
			if a > maxPrime:
				maxPrime = a
	
	return maxPrime

print "ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda"
print "The largest prime is", largestPrime("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda")