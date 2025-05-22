#!/usr/bin/python3

"""
Module 1-rectangle.py

Ce module définit 1classe rectangle qui a :
° deux attributs privés : __width et __height
° des getters et setters pour accéder à ces attributs avec des vérifications
° un constructeur __init__ qui accepte width et height en paramètres
"""


class Rectangle:
    """
    Classe Rectangle qui définit un rectangle
    avec des attributs privés et des accesseurs contrôlés
    """

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau rectangle.
        Args:
        ° width (int): largeur du rectangle (par défaut 0)
        ° height (int): hauteur du rectangle (par défaut 0)
        Raises:
        ° TypeError: si width ou height ne sont pas des entiers
        ° ValueError: si width ou height sont négatifs
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter de la largeur du rectangle.
        Retourne la valeur de l'attribut privé __width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter de la largeur avec vérifications :
        - doit être un entier
        - doit être >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter de la hauteur du rectangle
        Retourne la valeur de l'attribut privée __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter de la hauteur avec 2 vérifications :
        ° être un entier
        ° être sup ou égale à 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
