#!/usr/bin/python3
"""
Module task_02_requests
"""

import requests
import csv

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

def fetch_and_save_posts():
    """
    Fonction qui va  qui récuperer tous les messages dans le JSONPlaceholder
    """
    variable_reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    if variable_reponse.status_code == 200:
        print("Status Code: 200")
        variable_list_posts = variable_reponse.json()

        variable_donnees_filtrees = []
        for variable_un_post in variable_list_posts:
            variable_donnees_filtrees.append({
                "id": variable_un_post["id"],
                "title": variable_un_post["title"],
                "body": variable_un_post["body"]
                })
        with open("posts.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(variable_donnees_filtrees)

    else:
        print("Erreur", variable_reponse.status_code)
