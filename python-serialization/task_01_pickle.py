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
        ARGUMENTS : 
        ° name (str): Le nom de la personne.
        ° age (int): L'âge de la personne.
        ° is_student (bool): Le statut étudiant (True ou False).
        """
        self.name = name
        self.age = age
        self.is_student = is_student
        
        def display():
            """
            """
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Is Student: {is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(f)

    def deserialize(cls, filename):
        """
        """
        with open(filename, "rb") as f:
            pickle.load(CustomObject)
        

