#!/usr/bin/python3

def uppercase(str):
    resultat = ""  # initialisation chaîne vide au début

    for caractere in str:
        if ord(caractere) >= 97 and ord(caractere) <= 122:
            majuscule = chr(ord(caractere) - 32)
        else:
            majuscule = caractere

        resultat += majuscule

    print("{}".format(resultat))
