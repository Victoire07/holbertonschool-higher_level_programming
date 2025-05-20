#!/usr/bin/python3

"""
Module 1-square.py

Ce module définit 1classe Square qui definit 1 carré avc 1attrib privée : size
"""


class Square:
    """
    Classe représentant un carré
    """
    def __init__(self, size):
        """
        Initialse nouvelle instance de Square
        """
        self.__size = size
