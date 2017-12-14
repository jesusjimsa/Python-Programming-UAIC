# Write two functions to check if a number is prime,
# and check which of them is more time-efficient.

import time

def prime1(num):
	return all(num % i for i in xrange(2, num))

def prime2(num):
	solution = False

	if num > 1:
		for i in range(2,num):
			if (num % i) == 0:
				solution = False
			else:
				solution = True
	else:
		solution = False
	
	return solution

start_time = time.time()

prime1(234567)

print("--- %s seconds prime1 ---" % (time.time() - start_time))

start_time = time.time()

prime2(234567)

print("--- %s seconds prime2 ---" % (time.time() - start_time))