#!/usr/bin/python3
"""
Module task_03_xml.py
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire en XML et l'écrit dans un fichier.

    Args:
    ° dictionary (dict): Le dictionnaire à convertir.
    ° filename (str): Le nom du fichier XML à créer.
    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Lit un fichier XML et le convertit en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit à partir du fichier XML.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result    
