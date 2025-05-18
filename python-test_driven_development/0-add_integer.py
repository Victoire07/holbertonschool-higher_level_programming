#!/usr/bin/python3
"""
Ce module porte sur une fonction qui doit contenir 2 entiers

La fonction add_integer prend 2 nombres soit int soit float.
Si besoin elle convertit les float en int et retourne la somme.
Si arguments pas valides, exception avec TypeError.
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers ou flottants convertis en entiers.
    Retourne leur somme sous forme d'entier.
    Lève TypeError si un argument n’est pas un nombre.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
