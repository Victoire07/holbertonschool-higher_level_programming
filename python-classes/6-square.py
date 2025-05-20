#!/usr/bin/python3

"""
Module 6-square.py

Ce module va afficher la carré avec un décalage -->
° vers la droite (horizontalement, via des espaces)
° vers le bas (verticalement, via des lignes vides)
"""


class Square:
    """
    Classe représentant un carré avec contrôle pr sa taille
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un nouveau carré avec une taille donnée (par défaut 0).
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calcule et retourne aire du carré
        """
        return self.__size ** 2

    @property
    def size(self):
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

    @property
    def position(self):
        """
        Permet de récupérer la position du carré
        donc décalage horizontal et vertical
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Permet de modifier la position du carré, en vérifiant qu’il s’agit
        d’un tuple contenant deux entiers positifs (horizontal, vertical).

        Raises:TypeError: Si value n’est pas un tuple de 2 entiers positifs.
        """
        if not isinstance(value, (tuple)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], (int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        Affiche la carré avec le # selon la position
        """
        if self.size <= 0:
            print()
            return

        for _ in range(self.position[1]): #déclage verticale
                print()

        for _ in range(self.size): #affich carre lig par lig avec decalage ver
                print(" " * self.position[0] + "#" * self.size)
