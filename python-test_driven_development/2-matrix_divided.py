#!/usr/bin/python3
"""
Ce module a pour but de diviser tous les éléments donnés par un diviseur
"""
def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par `div`, arrondi à 2 décimales.
    La matrice doit être une liste de listes de int ou float
    Toutes les lignes doivent être de la même taille
    div doit être un nombre (int ou float) et ≠ de 0
    """
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
