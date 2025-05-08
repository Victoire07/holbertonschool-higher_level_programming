#!/usr/bin/python3
print("{}".format("".join(
    lettre for lettre in "abcdefghijklmnopqrstuvwxyz"
    if lettre != "e" and lettre != "q"
)))
