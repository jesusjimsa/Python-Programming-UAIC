# Write a function that receives a char_len integer and a
# variable number of strings (strings) and check that each
# two neighboring strings follow the following rule:
# the second string starts with the last char_len characters
# of the first string (like the word game pheasant).

def pheasant(ch_len, *strings):
	stringList = list()
	encadenado = True

	for one in strings:
		stringList.append(one)

	for i in range(0, len(stringList) - 1):
		lastPart = ""
		firstPart = ""

		for j in range(len(stringList[i]) - ch_len, len(stringList[i])):
			lastPart += stringList[i][j]
		
		for j in range(0, ch_len):
			firstPart += stringList[i + 1][j]
		
		if firstPart != lastPart:
			encadenado = False
			break

	return encadenado

if pheasant(3, "hivfohufuhf", "uhfipsgiypsigy", "igyihsfvbwdai", "daiwdvb"):
	print "Encadenado"
else:
	print "No encadenado"