# Write a function that receives as a parameter a variable
# number of lists and a whole number x. Return a list
# containing the items that appear exactly x times in the
# incoming lists. Example: For the [1,2,3], [2,3,4], [4,5,6],
# [4,1, "test"] and x = 2 lists [1,2,3 , 4] # 1 is in list 1
# and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2, 4 is in
# lists 2 and 3.

def xTimes(x, *lists):
	times = dict()
	timesList = list()

	for a in lists:
		for b in a:
			if b in times:
				times[b] += 1
			else:
				times[b] = 1
	
	auxTimes = dict(times)

	for c in times:
		if times[c] != x:
			del auxTimes[c]

	times = dict(auxTimes)

	for d in times:
		timesList.append(d)
	
	return timesList


print xTimes(2, [1,2,3], [2,3,4], [4,5,6], [4,1, "test"])