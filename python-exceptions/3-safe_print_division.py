#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        resultat_division = a / b
    except ZeroDivisionError:
        resultat_division = None
    finally:
        print("Inside result: {}".format(resultat_division))
    return (resultat_division)
