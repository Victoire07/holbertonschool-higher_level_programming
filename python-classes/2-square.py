#!/usr/bin/python3

"""
Module 2-square.py

Ce module définit une classe Square avec un attribut privé __size,
et valide que la taille est un entier positif ou nul!!
"""
class Square:
    """
    Classe représentant un carré avec taille privée validée
    """
    def __init__(self, size = 0):
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
        