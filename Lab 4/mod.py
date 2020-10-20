# ex7.1.py
# Create your own module in which to implement at least 3 functions.
# Use these functions in a script.


def sum(*nums):
    res = 0

    for a in nums:
        res += a

    return res


def hello():
    print("Not today")


def ItsWednesday():
    print("It's wednesday my dudes")
