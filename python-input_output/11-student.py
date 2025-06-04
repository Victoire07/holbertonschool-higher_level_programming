#!/usr/bin/python3
"""
Module 11-student.py
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

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant l'étudiant.
        Si attrs est une liste de chaînes, retourne uniquement
        les attributs listés
        Sinon, retourne tous les attributs.
        """
        if isinstance(attrs, list):

            attr_dic = {}
            for element in attrs:
                if isinstance(element, str) and hasattr(self, element):
                    attr_dic[element] = getattr(self, element)
            return attr_dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Remplace les attributs de l'étudiant par ceux du dictionnaire donné
        """
        for key, value in json.items():
            setattr(self, key, value)
