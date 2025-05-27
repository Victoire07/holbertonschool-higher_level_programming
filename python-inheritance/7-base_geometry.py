#!/usr/bin/python3
"""
Ce module définit une classe BaseGeometry
avec des méthodes de base de validation.
"""


class BaseGeometry:
    """
    Classe de base pour la geometie
    """
    def area(self):
        """
        Méthode qui lève une exception pour indiquer
        que le calcul de l'aire n'est pas encore implémenté.
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Valide que value est un entier strictement positif.
        Args: ° name: nom du champ (utilisé dans le message d'erreur)/
        ° value: valeur à valider
        Raises: °TypeError: si value n'est pas un int
        °ValueError: si value <= 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
