#!/usr/bin/python3
"""
Module task_02_csv.py
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
     Convertit un fichier CSV en un fichier JSON.

    Args:
    ° csv_filename (str): Le nom du fichier CSV à lire.

    Returns:
    ° bool: True si la conversion a réussi, False en cas d'erreur.
    """
    try:
        with open(csv_filename, "r") as csv_file:
            variable_reader = csv.DictReader(csv_file)
            variable_data = [row for row in variable_reader]  # Créer une liste de dictionnaires

        with open("data.json", "w") as json_file:
            json.dump(variable_data, json_file, indent=4)  # Écrire la liste dans le fichier JSON

        return True
    except Exception:
        return False
