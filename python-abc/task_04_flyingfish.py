#!/usr/bin/python3
class Fish:
    """
    Classe pour représenter un poisson
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")

class Bird:
    """
    Classe pour représenter un oiseau
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant,
    combinant les caractéristiques du poisson et de l’oiseau
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
