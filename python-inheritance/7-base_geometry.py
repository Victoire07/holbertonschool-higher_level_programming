#!/usr/bin/python3
"""
Ce module définit la classe BaseGeometry avec des méthodes de validation
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.
    Fournit des méthodes de validation de type et d'aire.
    """

    def area(self):
        """
        Méthode virtuelle qui lève une exception.
        Doit être surchargée par les classes filles.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que 'value' est un entier strictement positif.

        Args:
        ° name (str): Le nom du champ à valider.
        ° value (int): La valeur à valider.

        Raises:
        ° TypeError: Si 'value' n'est pas un entier.
        ° ValueError: Si 'value' est inférieur ou égal à 0.
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
