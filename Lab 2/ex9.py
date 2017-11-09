# Write a function that will order a list of string tuples
# based on the 3rd character of the 2nd element in the
# tuple. Example: [("abc", "bcd"), ("abc", "zza")] ==>
# [("abc", "zza"), ("abc", "bcd")]

def weirdOrder(list_of_tuples):
	ordered = list(list_of_tuples)

	ordered.sort(key = lambda a: a[1][2])

	return ordered

print weirdOrder([("abc", "bcd"), ("abc", "zza")])