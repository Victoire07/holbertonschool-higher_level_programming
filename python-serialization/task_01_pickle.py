#!/usr/bin/python3
"""
Module task_01_pickle.py
"""
import pickle


class CustomObject:
    """
    Classe représentant un objet personnalisé avec un nom, un âge,
    et un statut d'étudiant. Elle inclut des méthodes pour afficher
    ses attributs, les sérialiser et les désérialiser à l'aide de pickle.
    """
    def __init__(self, name, age, is_student):
        """
        Initialise un nouvel objet CustomObject.
        Args : 
        ° name (str): Le nom de la personne.
        ° age (int): L'âge de la personne.
        ° is_student (bool): Le statut étudiant (True ou False).
        """
        self.name = name
        self.age = age
        self.is_student = is_student
        
        
    def display(self):
        """
        Affiche les attributs de l'objet
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l'objet et l'enregistre dans un fichier.

        Args:
        ° filename (str): Le nom du fichier de sortie
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
         Désérialise un objet CustomObject depuis un fichier.

        Args:
        ° filename (str): Le nom du fichier d'entrée.

        Returns:
        ° CustomObject: L'objet désérialisé ou None si erreur
        """
        try:
            with open(filename, "rb") as f:
                return (pickle.load(f))
        except Exception:
            return (None)
