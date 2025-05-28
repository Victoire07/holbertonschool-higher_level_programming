#!/usr/bin/python3
"""
Le module porte sur la classe Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe qui hérite de BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur
        validées comme entiers strictement positifs.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
