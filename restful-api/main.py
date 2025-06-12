#!/usr/bin/python3
"""
Code pour fichier main généré par IA :)
"""


from http.server import HTTPServer
from task_03_http_server import API_Server

# Lancer le serveur sur le port 8000
server_address = ("", 8000)
httpd = HTTPServer(server_address, API_Server)
print("Serveur lancé sur http://localhost:8000")
httpd.serve_forever()
