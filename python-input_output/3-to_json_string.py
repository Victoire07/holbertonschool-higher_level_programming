#!/usr/bin/python3
"""
Module 3-to_json_string
"""
import json


def to_json_string(my_obj):
    """
    Fonction qui reçoit un objet Python (ex:liste,dictionnaire...)
    et retourne une chaîne de caractères représentant cet objet au format JSON
    """
    return json.dumps(my_obj)

