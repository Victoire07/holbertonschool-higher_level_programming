#!/usr/bin/python3
"""
Ce module a pour but d'afficher du texte avec une mise en page spéciale
"""


def text_indentation(text):
    """
    Affiche le texte avec 2 retours à la ligne après .,?:
    Supprime les espaces au début de chaque nouvelle ligne
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
