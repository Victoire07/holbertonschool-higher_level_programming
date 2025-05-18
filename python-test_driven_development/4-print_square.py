#!/usr/bin/python3
"""
Ce module a pour but d'afficher un carré avec des caractères dièzes(#)
"""


def print_square(size):
    """
    Va afficher un carré de size lignes et colonnes avec le caractère #
    size doit être un entier
    si < à 0 : ValueError
    si float : TypeError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print(size * "#")
