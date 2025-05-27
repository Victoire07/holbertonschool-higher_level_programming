#!/usr/bin/python3
"""
Ce module fournit une fonction qui renvoie
la liste des attributs et méthodes disponibles d'un objet
"""
def lookup(obj):
    """
    Fonction qui prend un paramètre obj
    Cette fonction doit retourner une liste de tous
    les attributs et méthodes de obj
    """
    return dir(obj)
