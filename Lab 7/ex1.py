# Write a program that will write the minutes run from the start, every x
# seconds, where x is random chosen at each iteration (from the interval
# [a, b], where a, b are arguments). The program will run infinitely.

import time, sys, random

a = int(sys.argv[1])
b = int(sys.argv[2])

start_time = time.time()

while True:
	time.sleep(random.randint(a, b))
	
	print "{:.2f}".format(((time.time() - start_time) / 60)), "minutes"