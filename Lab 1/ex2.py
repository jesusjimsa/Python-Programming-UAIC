# Write a function that calculates how many vowels are in a string.


def vowels(cadena):
    vocales = "aeiouAEIOU"
    count = 0

    for i in cadena:
        if(i in vocales):
            count += 1

    return count


print("Hay", vowels("Hola me llamo Jesus"), "vocales en la frase Hola me llamo Jesus")
