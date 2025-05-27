#!/usr/bin/python3
"""
Ce module fournit une fonction pour vérifier si un objet
est une instance d'une sous-classe d'une classe donnée
(mais pas de la classe elle-même)
"""


def inherits_from(obj, a_class):
    """
    Vérifie si obj est une instance d'une sous-classe de a_class
    (directement ou indirectement).
    Args: obj: L'objet à tester / a_class: La classe à comparer
    Returns: True si obj est une instance d'une classe qui hérite de a_class
    (mais pas a_class lui-même),False sinon.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return (True)
    else:
        return (False)
