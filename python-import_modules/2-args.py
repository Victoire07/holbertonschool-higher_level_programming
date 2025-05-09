#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb_args = len(sys.argv) - 1

    if nb_args == 0:
        print("0 arguments.")
    elif nb_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(nb_args))
        for nombre in range (1, len(sys.argv)):
            print("{}: {}".format(nombre, sys.argv[nombre]))
