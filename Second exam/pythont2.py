# Name: Jesus Jimenez Sanchez

import zipfile
import random
import urllib2

# Problem 1
# Implement the function problema1(n). The function receives one parameter n,
# natural number greater than 0. The functia will return a list with the first
# n natural numbers greater ( > ) than 10. For example problema1(3) will return [11,12,13]

def problema1(n):
	number_list = list()
	
	if n > 0:
		for i in range(11, 11 + n):
			number_list.append(i)
	
	return number_list

# Problem 2
# Implement the function problema2(big_string). The function receives one parameter big_string,
# a string. The function will return the length of the string. For example problema2(big_string="123456")
# will return 6.

def problema2(big_string):
	return len(big_string)

# Problem 3
# Implement the function problema3(x). The function receives one parameter X,
# natural number greater ( > ) than 1. The function will return the result of
# the polynom pow(X,4)+pow(X,3)+pow(x,2)+1. Where pow(x,2) is X to the power
# of 2. For example problema3(x=2) will return 29.

def problema3(x):
	if x > 1:
		return (x**4) + (x**3) + (x**2) + 1

# Problem 4
# Implement the function problema4(apath). The function receives one parameter
# apath the path to an archive. The function will return the number of files
# in the archive. For example problema4(apath="arhiva.zip") - where arhiva.zip
# contains ["file1.txt", "file2.exe","file3.dll","different_file.txt","different_file.exe"],
# will return 5 . Remark: the archive received as paramter will contain always only files
# in root without any folders or subfolders.

def problema4(apath):
	z = zipfile.ZipFile(apath)
	number_of_files = 0

	for i in z.infolist():
		number_of_files += 1
	
	return number_of_files

# Problem 5
# Implement the function problema5(n). The function receives one parameter n,
# natural number greater ( > ) than 0. The function will return a list with
# n real random numbers from the interval [0.0, 1.0). For example problema5(5)
# will return a list like [0.5570253572748867, 0.31369380280616177, 0.8721999476394512, 0.27726717948160373, 0.4449138851926042].

def problema5(n):
	lista = list()

	if n > 0:
		for i in range(0, n):
			lista.append(random.random())
	
	return lista

# Problem 6
# Implement the function problema6(alink). The function receives one parameter alink,
# an url. The function will return the length of the content from the link alink. For
# example problema6(alink="http://md5.jsontest.com/?text=example_text") will return 143

def problema6(alink):
	webpage = urllib2.urlopen(alink).read()

	return len(webpage)