#!/usr/bin/python3
"""
Module exercice task_00__abc
"""
from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Fais moi la docstring ici stp
    """
    @abstractmethod
    def sound(self):
        """
        Permet de décrire le bruit de l'animal (son cri)
        """
        pass
