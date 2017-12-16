# Name: Jesus Jimenez Sanchez

import sys, os
#import pdb; pdb.set_trace()

if sys.argv[0] == str(__file__):
	print sys.argv[-1]

def problema2():
	return 2 * 27

def problema3(n):
	to_str = str(n)
	suma = 0
	mult = 1

	for digit in to_str:
		suma += int(digit)
	
	for digit in to_str:
		mult *= int(digit)
	
	return suma > mult

def problema4(m):
	sol = list()

	for a in range(0, m):
		if not problema3(a):
			sol.append(a)

	return sol

def problema5(my_list):
	repeated = list()

	for a in my_list:
		if my_list.count(a) == 2:
			repeated.append(a)
		
	return repeated

# def problema6(folder, file):
# 	if os.path.exists(folder):
# 		try:
# 			fd = open(file, mode = "w")
# 		except OSError:
# 			print "Couldn't open/create", file
# 			return None

# 		for entry in os.listdir
