#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    liste_noms = dir(hidden_4)
    for nom in sorted(liste_noms):
        if not nom.startswith("__"):
            print(nom)
