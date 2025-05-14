#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        for nombre in ligne:
            print("{:d}".format(nombre), end=" ")

