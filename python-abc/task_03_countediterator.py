#!/usr/bin/python3
"""
Module exercice task_03_countediterator
"""


class CountedIterator:
    """
    Itérateur personnalisé qui compte le nombre d’éléments déjà parcourus
    """

    def __init__(self, iterable):
        """
        Initialise l’itérateur interne et le compteur à 0
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Retourne l’élément suivant et incrémente le compteur
        """
        valeur = next(self.iterator)
        self.count += 1
        return (valeur)

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà parcourus
        """
        return (self.count)
