#!/usr/bin/python3
"""
Module représentant une classe Rectangle dérivée de BaseGeometry
Cette classe permet de créer des rectangles avec des attributs de largeur et 
hauteur, tout en s'assurant que ces dimensions sont des entiers positifs
"""


class BaseGeometry:
    """
    Classe de base pour la geometie
    """
    def area(self):
        """
        Méthode qui lève une exception pour indiquer
        que le calcul de l'aire n'est pas encore implémenté.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que value est un entier strictement positif.
        Args: ° name: nom du champ (utilisé dans le message d'erreur)/
        ° value: valeur à valider
        Raises: °TypeError: si value n'est pas un int
        °ValueError: si value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur
        validées comme entiers strictement positifs.
        """
        self.__width = width
        self.__height = height
