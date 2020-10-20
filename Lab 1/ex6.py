#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Write a function that converts a string of
# characters written in UpperCamelCase into
# lowercase_with_underscores.


def lowecaseUnder(unString):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    continuar = False

    for i in range(1, len(unString)):
        if unString[i] in upper and not continuar:
            unString = unString[:i] + '_' + unString[i:]    # Para insertar la barra baja antes de la mayúscula
            continuar = True
        else:
            continuar = False

    unString = unString.lower()

    return unString


print("UpperCamelCase se convierte en", lowecaseUnder("UpperCamelCase"))
