#!/usr/bin/python3
"""
task_00_basic_serialization.py
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON
    """
    with open(filename, "w") as f:
        json.dump(data, f)
