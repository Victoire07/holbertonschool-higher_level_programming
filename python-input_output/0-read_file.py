#!/usr/bin/python3
"""
Module 0-read_file.py
"""


def read_file(filename=""):
    """
    Lit un fichier texte (UTF-8) et affiche son contenu sur la sortie standard
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
