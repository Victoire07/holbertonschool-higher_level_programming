#!/usr/bin/python3
"""
Module task_02_requests
"""

import requests

def fetch_and_print_posts():
    """
    Fonction qui va afficher chaque titre de post
    """
    variable_reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    if variable_reponse.status_code == 200:
        print("Status Code: 200")
        variable_liste_posts = variable_reponse.json()
        for variable_un_post in variable_liste_posts:
            print(variable_un_post["title"])
    else:
        print("Erreur", variable_reponse.status_code)
