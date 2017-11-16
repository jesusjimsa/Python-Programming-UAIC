# With the global dictionary:
#
#	{
# 		"+": lambda a, b: a + b,
# 		"*": lambda a, b: a * b,
# 		"/": lambda a, b: a / b,
# 		"%": lambda a, b: a % b
# 	}
#
# Build an apply_operator function (operator, a, b)
# that will apply over a and b the rule specified
# by the global dictionary. Implement it so that if
# a new operator is added, it is not necessary to
# change the function.


global_dict = {
	"+": lambda a, b: a + b,
	"*": lambda a, b: a * b,
	"/": lambda a, b: a / b,
	"%": lambda a, b: a % b
}

def apply_operator(operator, a, b):
	return global_dict[operator](a, b)

print apply_operator("*", 2, 2)
