#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for ligne in matrix:
        ligne_au_carree = map(lambda x: x**2, ligne)
        new_matrix.append(ligne_au_carree)
        return(new_matrix)
