#!/usr/bin/python3
"""
Ce module définit la classe MyList qui hérite de list
et ajoute une méthode pour afficher la liste triée.
"""


class MyList(list):
    """
    MyList est une sous-classe de list qui ajoute des fonctionnalités
    supplémentaires
    Elle se comporte comme une liste normale avec une méthode
    pour imprimer les éléments dans l'ordre croissant
    """
    def print_sorted(self):
        """
        Imprime les éléments de la liste dans l'ordre croissant.
        Cette méthode ne retourne rien et modifie l'affichage seulement.
        """
        print(sorted(self))
