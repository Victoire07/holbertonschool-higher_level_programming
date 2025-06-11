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
    


