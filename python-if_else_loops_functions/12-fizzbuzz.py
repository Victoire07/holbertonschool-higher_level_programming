#!/usr/bin/python3
def fizzbuzz():
    for nombre in range(1, 101):
        if nombre % 3 == 0 and nombre % 5 == 0:
            print("FizzBuzz", end=" ")
        elif nombre % 3 == 0:
            print("Fizz", end=" ")
        elif nombre % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(nombre, end=" ")
