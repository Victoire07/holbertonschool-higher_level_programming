#!/usr/bin/python3
"""
Module 5-save_to_json_file.py
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Fonction qui prend un objet Python (ex:une liste ou un dictionnaire)
    et l’enregistre dans un fichier texte sous forme JSON
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
