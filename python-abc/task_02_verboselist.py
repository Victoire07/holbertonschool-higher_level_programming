#!/usr/bin/python3
"""
Module exercice task_02_verboselist
"""


class VerboseList(list):
    """
    Classe personnalisée VerboseList qui hérite de la classe Python list,
    mais affiche un message à chaque ajout ou suppression d’un élément
    """
    def append(self, item):
        """
        Ajoute un élément à la liste et affiche un message
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Étend la liste avec plusieurs éléments et affiche un message
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")
