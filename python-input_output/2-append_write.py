#!/usr/bin/python3
"""
Module 2-append_write.py
"""


def append_write(filename="", text=""):
    """
    Fonction qui ajoute du texte à la fin d’un fichier texte (encodé en UTF-8)
    et retourne le nombre de caractères ajoutés
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
