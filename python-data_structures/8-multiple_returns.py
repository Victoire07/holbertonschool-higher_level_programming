#!/usr/bin/python3
def multiple_returns(sentence):
    longueur = len(sentence)
    if (len(sentence) == 0):
        premier = None
    else:
        premier = sentence[0]
    return (longueur, premier)
