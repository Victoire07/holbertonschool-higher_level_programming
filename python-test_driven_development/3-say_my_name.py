#!/usr/bin/python3
"""
Ce module a pour but d'afficher le prénom et le nom
"""

def say_my_name(first_name, last_name=""):
    """
    Va afficher 'My name is <first_name> <last_name>'.
    Les deux paramètres doivent être des chaînes de caractères.
    """
    if not isinstance (first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance (last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
