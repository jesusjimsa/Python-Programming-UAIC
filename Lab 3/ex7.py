# Consider a globally defined dictionary similar to the one above,
# with the difference that the functions given as values of the
# dictionary can receive any combination of parameters. Write a
# function apply_function that receives as a parameter the name of
# an operation and applies the corresponding function over the
# arguments received. Implement it so that if a new function is
# added, it is not necessary to change the function apply_function.


global_dict = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}

translation = {
    "add": "+",
    "times": "*",
    "divided by": "/",
    "module": "%"
}


def apply_operator(a, b, c):
    if isinstance(a, basestring):
        return global_dict[translation[a]](b, c)
    if isinstance(b, basestring):
        return global_dict[translation[b]](a, c)
    if isinstance(c, basestring):
        return global_dict[translation[c]](a, b)


print(apply_operator(2, "add", 2))
