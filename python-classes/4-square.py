#!/usr/bin/python3

"""
Module 4-square.py

Ce module définit une classe Square avec :
- un attribut privé __size
- une méthode area() pour calculer l’aire
- un getter et un setter pour accéder/modifier size avec vérification
"""

class Square:
    """
    Classe représentant un carré avec contrôle pr sa taille
    """
    def __init__(self, size=0):
        """
        Initialise un nouveau carré avec une taille donnée (par défaut 0).
        """
        self.size = size
    def area(self):
        """
        Calcule et retourne aire du carré
        """
        return self.__size ** 2
    @property
    def size (self):
        """
        Permet de récupérer l'aire du carré!
        """
        return self.__size
    @size.setter
    def size(self, value):
        """
        Permet de modifier la taille du carré et aussi de verifier
        si il est valide
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

