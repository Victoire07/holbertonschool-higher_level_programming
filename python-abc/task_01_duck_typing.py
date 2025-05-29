#!/usr/bin/python3
"""
Module exercice task_01_duck_typing
"""
from abc import ABC, abstractmethod
import math
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
    @abstractmethod
    def perimeter(self):
        """
        Permet de calculer le périmètre
        """
        pass

class Circle(Shape):
    """
    Classe représentant un cercle, héritant de la classe abstraite Shape.

    Cette classe permet de calculer l'aire et le périmètre d’un cercle
    à partir de son rayon. Elle implémente les méthodes area() et perimeter().
    """
    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné
        """
        self.radius = radius
    def area(self):
        """
        Retourne la surface du cercle
        """
        return (math.pi * self.radius * self.radius)
    def perimeter(self):
        """
        Retourne le périmètre du cercle
        """
        return (2 * math.pi * self.radius)

class Rectangle(Shape):
    """
    Classe représentant un rectangle héritée dla classe abstraite Shape
    Son constructeur doit accepter la largeur et la hauteur. 
    Sont impléméntées les méthodes area et perimeter.
    """
    def __init__():
        """
        """
    




