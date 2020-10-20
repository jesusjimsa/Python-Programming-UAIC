# Write a function that checks whether a character string
# contains special characters (\r, \t, \n, \a, \b, \f, \v)


def specialChar(unString):
    specials = ["\r", "\t", "\n", "\a", "\b", "\f", "\v"]
    contained = False

    for i in unString:
        if i in specials:
            contained = True

    return contained


def imprimeRes(contenido):
    if contenido:
        print("Contiene caracteres especiales\n")
    else:
        print("No contiene caracteres especiales\n")


stringo = "Este string de prueba \r contiene varios \b caracteres \f especiales\n"
strindos = "Este no los contiene"

print("El primer string es:")
print(stringo)

imprimeRes(specialChar(stringo))

print("El segundo string es:")
print(strindos)

imprimeRes(specialChar(strindos))
