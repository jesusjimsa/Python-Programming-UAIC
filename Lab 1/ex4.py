# Write a function that receives two strings as parameters and
# returns the number of occurrences of the first character string
# in the second.


def charOcurrences(unString, otroString):
    fiChar = unString[0]
    ocurrences = 0

    for charac in otroString:
        if charac == fiChar:
            ocurrences += 1

    return ocurrences


priString = raw_input("Introducir una frase: ")
segString = raw_input("Introducir una segunda frase: ")

print("El primer caracter de la primera frase es", priString[0], "y aparece", charOcurrences(priString, segString),
      "veces en la segunda frase")