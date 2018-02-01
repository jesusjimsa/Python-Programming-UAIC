# Problem 1
# Implement the function problema1(n). The function receives 1 parameter n,
# a natural number greater than 0 and smaller than 90. The function will
# return a list with the first n natural numbers smaller ( < ) than 100.
# For example problema1(3) will return [99,98,97].

import zipfile
import random
import urllib2

def problema1(n):
	smaller_than_100 = list()

	if 0 < n and n < 90:
		for i in range(0, n):
			smaller_than_100.append(99 - i)
		
	return smaller_than_100

print problema1(3)

# Problem 2
# Implement the function problema2(alist). The function receives one parameter
# alist, a list. The function will return the length of the list. For example
# problema2(alist = [1,2,3,4,5,6]) will return 6.

def problema2(alist):
	return len(alist)

print problema2([1,2,3,4,5,6])

# Problem 3
# Implement the function problema3(x). The function receives one parameter X,
# natural number greater than ( > ) 1. The function will return the result of
# the expresion x * (x + 2) - 3 * x. For example problema3(x = 2) will return 2.

def problema3(x):
	return x * (x + 2) - 3 * x

print problema3(2)

# Problem 4
# Implement the function problema4(apath). The function receives one parameter apath,
# the path to an archive. The function will return True if inside the arhives
# there is a file named test.py and False otherwise. For example 
# problema4(apath = "arhiva.zip"), where arhiva.zip contains
# ["file1.txt", "file2.exe", "file3.dll", "different_file.txt", "different_file.exe"]
# will return False. Observation: the given archives contain on files, no folders
# or subfolders.

def problema4(apath):
	try:
		z = zipfile.ZipFile(apath)
	except Exception as e:
		print "Error -->", e
	else:
		for i in z.infolist():
			if i.filename == "test.py":
				return True

		return False

print problema4("./archive.zip")

# Problem 5
# Implement the function problema5(a,b). The function receives two parameters a,b,
# natural numbers greater than zero and a < b. The function will return a random number
# from the inverval [a, b]. For example problema5(5, 10) can return 7 when called.

def problema5(a,b):
	rand_number = -1

	if a > 0 and b > 0 and a < b:
		rand_number = random.randint(a, b)
	
	return rand_number

print problema5(5, 10)

# Problem 6
# Implement the function problema6(alink). The function receives one parameter alink, a
# url. The function will return the first 9 caraters from the content of the url alink.
# For exemple problema6(alink = "https://profs.info.uaic.ro/~gdt/") will return "<!DOCTYPE".

def problema6(alink):
	first_nine = ""

	try:
		webpage = urllib2.urlopen(alink).read()
	except Exception as e:
		print "Error -->", e
	else:
		for i in range(0, 9):
			first_nine = first_nine + webpage[i]
	
	return first_nine

print problema6("https://profs.info.uaic.ro/~gdt/")

# Problem 7
# Implement the function problema7(astr). The function receives a parameter astr, a string.
# The function will return True if astr begins with 5 digits and False otherwise. For
# example problema6(astr="12345 is a valid string") will return True and
# problema6(astr=".12345 is not a valid string") will return False.

def problema7(astr):
	digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

	if (astr[0] in digit) and (astr[1] in digit) and (astr[2] in digit) and (astr[3] in digit) and (astr[4] in digit):
		return True
	else:
		return False

print problema7("12345 is a valid string")