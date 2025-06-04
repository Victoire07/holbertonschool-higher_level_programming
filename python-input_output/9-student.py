#!/usr/bin/python3
"""
Module 9-student.py
"""


class Student():
    """
    Classe représentant 1 élève avec nom, prénom et âge
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialise un étudiant avec son prénom, nom et âge
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne un dictionnaire représentant les attributs de l'étudiant
        """
        return self.__dict__
