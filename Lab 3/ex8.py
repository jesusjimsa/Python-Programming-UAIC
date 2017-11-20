# Write a function that receives as a parameter a set and returns a
# tuple (a, b), representing the number of unique elements in the
# set, and b representing the number of duplicate elements in the set.

def countSet(setcillo):
	return tuple((len(setcillo), len(setcillo)))	# Sets have no repeated elements...

hola = set([1, 2, 3, 4, 56, 7, 8, 0, 876543, 23, 456, 78, 76, 543, 7, 89, 876, 543, 2, 3, 456, 78])
print countSet(hola)
