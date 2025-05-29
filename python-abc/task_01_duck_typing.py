#!/usr/bin/python3
"""
Module exercice task_01_duck_typing
"""
from abc import ABC, abstractmethod
class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.

    Cette classe définit l'interface que toutes les formes doivent implémenter,
    notamment les méthodes `area` pour calculer la surface et `perimeter`
    pour calculer le périmètre. Elle sert de modèle commun pour toutes
    les formes géométriques (cercle, rectangle, etc.).
    """
    @abstractmethod
    def area(self):
        """
        Permet de calculer la surface
        """
    def perimeter(self):
        """
        Permet de calculer le périmètre
        """
        pass


