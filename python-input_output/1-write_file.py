#!/usr/bin/python3
"""
Module 1-write_file.py
"""


def write_file(filename="", text=""):
    """
    Écrit une chaîne de caractères dans un fichier texte (encodé en UTF-8) et
    retourne le nombre de caractères qui ont été écrits
    """

    with open(filename, "w", encoding="utf_8") as f:
        return (f.write(text))
