#!/usr/bin/python3

def print_last_digit(number):
    valeur_absolue = abs(number)
    dernier_chiffre = valeur_absolue % 10
    print("{}".format(dernier_chiffre), end="")
    return dernier_chiffre
