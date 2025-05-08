#!/usr/bin/python3
print("{}".format("".join(
    chr(lettre) for lettre in range(97, 123)
    if lettre != 101 and lettre != 113
)))
