#!/usr/bin/python3
"""
Module 4-from_json_string.py
"""
import json


def from_json_string(my_str):
    """
    Fonction qui reçoit une chaîne de caractères au format JSON
    et renvoie l’objet Python correspondant (liste, dictionnaire...)
    """
    return json.loads(my_str)
