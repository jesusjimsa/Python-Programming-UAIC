# Write a python program to receive two numbers from the command line (a and b) and display:
# a) a - b
# b) a + b
# c) a / b
# d) a * b

#import pdb; pdb.set_trace()

first = int(raw_input("Insert the first number: "))
second = int(raw_input("Insert the second number: "))

try:	# Check if the input is correct
	int(first)
except ValueError:
	print "The input was not correct, it has to be an integer"
	sys.exit()

try:	# Check if the input is correct
	int(second)
except ValueError:
	print "The input was not correct, it has to be an integer"
	sys.exit()

try:
	sub = first - second
	add = first + second
	mult = first * second
	div = first / second
except ArithmeticError:
	print "One of the operations could not be completed"
	sys.exit()
else:
	print first, "-", second, "=", sub
	print first, "+", second, "=", add
	print first, "*", second, "=", mult
	print first, "/", second, "=", div