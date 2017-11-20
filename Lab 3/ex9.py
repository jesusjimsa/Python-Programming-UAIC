# Write a function that receives a variable number of sets and returns
# a dictionary with the following operations from all sets two by two:
# reunion, intersection, a - b, b - a. The key will have the following
# form: "a op b", where a and b are two sets, and op is the applied
# operator: |, &, -.
#
# Ex: {1,2}, {2, 3} =>
# 
# {
#	"{1, 2} | {2, 3}": 3,
# 	"{1, 2} & {2, 3}": 1,
# 	"{1, 2} - {2, 3}": 1,
# 	...
# }

#import pdb; pdb.set_trace()

def operationsSet(*conjuntos):
	solution = dict()
	first = True
	stringUnion = ""
	stringIntersection = ""
	stringSub1 = ""
	stringSub2 = ""
	
	# Construct keys
	for a in conjuntos:
		stringUnion += "{" + str(a) + "} | "
		stringUnion = stringUnion.replace("set([", "")
		stringUnion = stringUnion.replace("])", "")
		stringIntersection += "{" + str(a) + "} & "
		stringIntersection = stringIntersection.replace("set([", "")
		stringIntersection = stringIntersection.replace("])", "")
		stringSub1 += "{" + str(a) + "} - "
		stringSub1 = stringSub1.replace("set([", "")
		stringSub1 = stringSub1.replace("])", "")
	
	for a in reversed(conjuntos):
		stringSub2 += "{" + str(a) + "} - "
		stringSub2 = stringSub2.replace("set([", "")
		stringSub2 = stringSub2.replace("])", "")

	# Delete extra characters
	stringUnion = stringUnion[0:len(stringUnion) - 3]
	stringIntersection = stringIntersection[0:len(stringIntersection) - 3]
	stringSub1 = stringSub1[0:len(stringSub1) - 3]
	stringSub2 = stringSub2[0:len(stringSub2) - 3]
	
	# Construct the dictionary
	for a in conjuntos:
		if not first:
			solution[stringUnion] |= set(a)
			solution[stringIntersection] &= set(a)
			solution[stringSub1] -= set(a)
		else:
			first = False
			solution[stringUnion] = set(a)
			solution[stringIntersection] = set(a)
			solution[stringSub1] = set(a)

	first = True

	for b in reversed(conjuntos):
		if not first:
			solution[stringSub2] -= set(b)
		else:
			first = False
			solution[stringSub2] = set(b)

	return solution

se = set([1, 2, 3, 4, 5])
et = set([2, 3, 4, 5, 6])

jeje = operationsSet(se, et)

for d in jeje:
	print d + ":" + str(jeje[d])