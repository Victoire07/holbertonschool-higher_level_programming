#!/usr/bin/python3

"""
Module 3-square.py

Ce module définit une classe Square avec :
- un attribut privé __size
- une vérification de type et de valeur lors de l’instanciation
- une méthode area() pour calculer l’aire du carré
"""

class Square:
    """
    Classe représentant un carré avec taille privée validée
    """
    def __init__(self, size=0):
        """
        Initialise un carré avec une taille.
        Args: size (int): La taille du carré (doit être un entier >=0)
        Raises:TypeError: Si size n'est pas un entier ou ValueError:
        Si size est < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Retourne l'aire du carré
        """
        return (self.__size ** 2)
