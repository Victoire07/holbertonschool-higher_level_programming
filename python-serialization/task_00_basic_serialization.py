#!/usr/bin/python3
"""
task_00_basic_serialization.py
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON:
    ° data (dict): Le dictionnaire à sérialiser.
    ° filename (str): Le nom du fichier où enregistrer les données.
    """
    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charge les données sérialisées à partir d'un fichier JSON
    et les désérialise en un dictionnaire Python
    """
    with open(filename, "r") as f:
        data = json.load(f)
        return (data)
