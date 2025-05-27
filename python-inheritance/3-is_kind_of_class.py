#!/usr/bin/python3
"""
Ce module contient une fonction qui vérifie si un objet
est une instance d'une classe ou d'une classe dérivée.
"""


def is_kind_of_class(obj, a_class):
    """
    Vérifie si l'objet est une instance de la classe spécifiée
    ou d'une classe qui en hérite.
    Args: obj: l'objet à tester / a_class: la classe à comparer
    Returns:True si obj est une instance de a_class ou d'une classe fille,
    False sinon.
    """
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
