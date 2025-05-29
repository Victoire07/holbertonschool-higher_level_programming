#!/usr/bin/python3
"""
Module exercice task_00__abc
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Classe abstraite représentant un animal.

    Cette classe impose aux sous-classes de définir la méthode `sound`,
    qui permet de décrire le cri ou le son émis par l'animal.
    """
    @abstractmethod
    def sound(self):
        """
        Permet de décrire le bruit de l'animal (son cri)
        """
        pass

class Dog(Animal):
    """
    Classe représentant un chien, héritant de la classe abstraite Animal.

    Cette classe implémente la méthode `sound` pour retourner
    le son spécifique du chien
    """
    def sound(self):
        """
        Permet l'aboiement du chien
        """
        return ("Bark")
    
class Cat(Animal):
    """
    Classe pour représenter le chat héritant de la classe abstraite Animal
    Cette classe implémente sound pour retourner le miaulement du chat
    """
    def sound(self):
        """
        Permet le miaulement du chat
        """
        return ("Meow")
