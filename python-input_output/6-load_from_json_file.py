#!/usr/bin/python3
"""
Module 6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
    Charge un objet Python à partir d’un fichier JSON
    """
    with open(filename, "r") as f:
        return json.load(f)
