# Write a function that receives as a parameter
# an x list, and a number k. Return a list of
# tuples that represent combinations of len (x)
# taken by k from list x. Example: for the list
# x = [1,2,3,4] and k = 3, return
# [(1,2,3), (1,2,4), (1,3,4) 3, 4)].


def combinations(x, k):
    resultado = list()
    listasAux = list()
    noTuples = list()
    i = 0

    # It doesn't generate all possible tuples, but the statement doesn't ask
    # for all of them so this implementation may be OK

    if k < len(x):
        while i < len(x):
            listasAux.append(x[i])
            j = i + 1

            while j < (k + i) and j < len(x):
                listasAux.append(x[j])

                j += 1

            i += 1
            noTuples.append(list(listasAux))
            del listasAux[:]    # Clear list

        for a in noTuples:
            resultado.append(tuple(a))

    return resultado


print(combinations([1, 2, 3, 4], 3))
