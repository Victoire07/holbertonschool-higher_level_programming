#!/usr/bin/python3
"""
Module 7-add_item.py
"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Nom du fichier JSON dans lequel je veux save la liste
filename = "add_item.json"


# Essayer de charger la liste déjà existante dans le fichier JSON
# Si le fichier n'existe pas ou est vide commencer avec liste vide
try:
    items = load_from_json_file(filename)
except Exception:
    items = []

# Récupération des arguments passés au script (après nom fichier lui mm)
args_to_add = sys.argv[1:]

# ajoute tous les nouveaux arguments à la liste existante
items.extend(args_to_add)

# sauvegarde la liste mise à jour dans le fichier JSON
save_to_json_file(items, filename)
