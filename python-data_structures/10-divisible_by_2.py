#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultat = []
    for nombre in my_list:
        if nombre % 2 == 0:
            resultat.append(True)
        else:
            resultat.append(False)
    return (resultat)

