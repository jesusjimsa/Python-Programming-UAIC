# The validate_dict function that receives as a parameter
# a set of tuples that represent validation rules for a
# dictionary with string keys and values of the string
# type and a dictionary. A rule is defined as follows:
# (key, "prefix", "middle", "suffix"). A value is considered
# valid if it starts with "prefix", "middle" is inside the
# value (not at the beginning or end) and ends with "suffix".
# The function will return True if the given dictionary
# matches all the rules, False otherwise.
# Example: the rules [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")]
# {"key1": "come inside, it's too cold out", "key3": "this is not valid"} =>
# False because although the rules are respected for "key1" and "key2" "key3"
# that does not appear in the rules.

def validate_dict(setTuples, dicc):
	for a, b in zip(setTuples, dicc):
		if a[0] == b:
			if not ((a[1] == dicc[b][0:len(a[1])]) and (a[2] in dicc[b]) and (a[3] == dicc[b][len(dicc[b]) - len(a[3]):len(dicc[b])])):
				return False
		else:
			return False

	return True

if validate_dict([("key1", "come", "inside", "out"), ("key2", "this", "not", "lid")], {"key1": "come inside, it's too cold out", "key2": "this is not valid"}):
	print "Si"
else:
	print "No"
