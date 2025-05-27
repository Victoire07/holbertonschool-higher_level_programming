#!/usr/bin/python3
"""
Fonction qui renvoie True si l'objet est exactement une instance de la classe
spécifiée ; sinon False
"""


def is_same_class(obj, a_class):
    """
    Vérifie si l'objet est exactement une instance de la classe spécifiée
    """
    if type(obj) == a_class:
        return (True)
    else:
        return (False)
