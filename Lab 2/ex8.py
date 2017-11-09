# Write a function that receives a variable number of lists
# and returns a list of tuples as follows: the first tuple
# contains the first items in the lists, the second element
# contains the items on the position 2 in the lists, etc.
# Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return:
# [(1.5, a " , 6, "b"), (3,7, "c")]. Note: If input lists do
# not have the same number of items, missing items will be 
# eplaced with None to be able to generate max ([len(x) for
# x in input_lists]) tuples.

def tupleList(*lists):
	elements = list()
	aux = list()

	for a in range(0, len(lists)):
		for b in lists:
			try:
				aux.append(b[a])
			except IndexError:
				aux.append(None)
			
		
		elements.append(tuple(aux))
		del aux[:]	# Clear aux
	
	return elements

print tupleList([1, 2, 3], [5, 6, 7], ["a", "b", "c"])