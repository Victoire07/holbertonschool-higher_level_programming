#!/usr/bin/python3
"""
Ce module définit une classe Square qui hérite de Rectangle.
Il représente un carré dont la taille est validée comme un entier
strictement positif à l’aide de la méthode integer_validator héritée.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Représente un carré, avec largeur et hauteur identiques.
    Hérite de Rectangle.
    """
    def __init__(self, size):
        """
        Initialise un carré avec une taille donnée.
        La taille est validée comme un entier strictement positif,
        puis transmise au constructeur parent Rectangle en tant que
        largeur et hauteur identiques.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return (f"[Square] {self.__width}/{self.__height}")
