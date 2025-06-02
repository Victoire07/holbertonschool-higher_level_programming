#!/usr/bin/python3

def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et affiche son contenu sur la sortie standard
    """
    with open(filename, "r") as f:
        for ligne in f:
            print(ligne)
