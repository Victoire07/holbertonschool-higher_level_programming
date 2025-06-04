#!/usr/bin/python3
"""
Module 8-class_to_json.py
"""


def class_to_json(obj):
    """
    Renvoie la description du dictionnaire pour la sérialisation JSON d1 objet
    """
    return obj.__dict__


