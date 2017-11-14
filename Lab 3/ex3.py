# Compare two dictionaries without using the operator
# "==" and return a list of differences as follows:
# {common keys but with different values, the keys
# that are only found in the first dict, the keys
# that are only found in the second dict}
# (Attention, dictionaries must be recursively covered
# because they can contain other containers, such as
# dictionaries, lists, sets, etc.)

def cmpDict(undict, otrodict):
	commonKeys = list()
	keysInFirst = list()
	keysInSecond = list()
	allKeys = list()

	for a in undict:
		if a in otrodict:
			commonKeys.append(a)
		else:
			keysInFirst.append(a)
	
	for b in otrodict:
		if b not in undict:
			keysInSecond.append(b)
	
	allKeys.append(commonKeys)
	allKeys.append(keysInFirst)
	allKeys.append(keysInSecond)

	return allKeys

def characterCounter(cadena):
	counter = dict()

	for i in range(0, len(cadena)):
		if cadena[i] in counter:
			counter[cadena[i]] += 1
		else:
			counter[cadena[i]] = 1

	return counter

print cmpDict(characterCounter("Ana has apples"), characterCounter("Joe has oranges"))