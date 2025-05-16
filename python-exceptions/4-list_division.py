#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resultats = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            resultats.append(a / b)
        except(IndexError):
            print("out of range")
            resultats.append(0)
        except(ZeroDivisionError):
            print("division by 0")
            resultats.append(0)
        except(TypeError):
            print("wrong type")
            resultats.append(0)
        finally:
            pass
    return (resultats)
