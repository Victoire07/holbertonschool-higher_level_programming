#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    dico_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    valeur_precedente = 0
    for char in reversed(roman_string):
        value = dico_roman.get(char, 0)
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return (total)
