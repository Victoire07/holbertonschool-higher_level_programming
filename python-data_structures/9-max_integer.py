#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    max_valeur = my_list[0]

    for nombre in my_list[1:]:
        if nombre > max_valeur:
            max_valeur = nombre

    return max_valeur
