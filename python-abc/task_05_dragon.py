#!/usr/bin/python3
"""
Module exercice task_05_dragon
"""
class SwimMixin:
    """
    Mixin ajoutant la capacité de nager à une classe
    """
    def swim(self):
        """
        Affiche que la créature nage
        """
        print("The creature swims!")

class FlyMixin:
    """
    Mixin ajoutant la capacité de voler à une classe
    """
    def fly(self):
        """
        Print que la créature vole
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Classe Dragon combinant les capacités de nager et voler
    """
    def roar(self):
        """
        Print que le dragon rugit
        """
        print("The dragon roars!")

    