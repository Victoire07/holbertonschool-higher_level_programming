#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nouvelle_list = []
    for element in my_list:
        if element == search:
            nouvelle_list.append(replace)
        else:
            nouvelle_list.append(element)
    return (nouvelle_list)
