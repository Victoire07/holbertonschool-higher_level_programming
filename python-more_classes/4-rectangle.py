#!/usr/bin/python3

"""
Module 4-rectangle.py

Ce module définit une classe Rectangle avec :
- deux attributs privés : __width et __height
- des getters et setters avec vérification de type/valeurs
- un constructeur avec arguments optionnels
- une méthode area() qui retourne l’aire
- une méthode perimeter() qui retourne le périmètre (0 si width ou height est nul)
- la méthode __str__ qui retourne une représentation textuelle du rectangle avec des '#'
- la méthode __repr__ qui retourne une chaîne permettant de recréer un objet identique avec eval()
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

    def area(self):
        """
        Permet de calculer l'aire du rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Permet de calculer le périmètre du rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * (self.__height + self.__width))

    def __str__(self):
        """
        Retourne une représentation textuelle du rectangle avec des '#'
        Chaque ligne correspond à la hauteur du rectangle,
        et chaque ligne contient 'width' caractères '#'.
        Si width ou height est nul, retourne une chaîne vide.
        """
        if (self.__width) == 0 or (self.__height) == 0:
            return ("")
        else:
            return ("\n".join(["#" * self.__width] * self.__height))

    def __repr__(self):
        """
        Retourne une chaîne de texte représentant le rectangle
        sous la forme : Rectangle(width, height)
        Cette chaîne doit permettre de recréer un objet identique
        via la fonction eval().
        """
        return (f"Rectangle({self.width}, {self.height})")
