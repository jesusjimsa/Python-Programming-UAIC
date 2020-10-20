# Write a function that receives as parameters two
# lists a and b and returns a set of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)


def twoLists(aList, bList):
    everyting = set(set())
    aSet = frozenset(aList)
    bSet = frozenset(bList)

    everyting.add(aSet.union(bSet))
    everyting.add(aSet.intersection(bSet))
    everyting.add(aSet.difference(bSet))
    everyting.add(bSet.difference(aSet))

    return everyting


print(twoLists([3, 5, 7, 9], [3, 4, 5, 6, 7, 8, 9]))
