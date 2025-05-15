#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    score_max = 0
    nom_associe = ""
    for key, value in a_dictionary.items():
        if value > score_max:
            score_max = value
            nom_associe = key
    return (nom_associe)
