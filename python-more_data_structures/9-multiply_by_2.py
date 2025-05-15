#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nouveau_dico = {}
    for key, value in a_dictionary.items():
        nouvelle_valeur = value * 2
        nouveau_dico[key] = nouvelle_valeur
    return(nouveau_dico)
