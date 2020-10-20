# Write a function that receives as parameters two
# lists a and b and returns: (a intersected with b,
# a reunited with b, a - b, b - a)


def listThings(aList, bList):
    everyting = list()
    intersection = list()
    union = list()
    a_menos_b = list(aList)
    b_menos_a = list(bList)		# They need list(...) because if I just use = they will be the same object

    # Intersection
    for b in bList:
        if b in aList:
            intersection.append(b)

    intersection.sort()
    
    # This turns the list into a set to remove repeated elements and then back to a list
    intersection = list(set(intersection))

    # Union
    union = list(aList)

    for b in bList:
        union.append(b)

    union.sort()

    # a - b
    for b in bList:
        if b in aList:
            a_menos_b.remove(b)
    # b - a
    for a in aList:
        if a in bList:
            b_menos_a.remove(a)

    everyting.append(intersection)
    everyting.append(union)
    everyting.append(a_menos_b)
    everyting.append(b_menos_a)

    return everyting


print(listThings([3, 5, 7, 9], [3, 4, 5, 6, 7, 8, 9]))
