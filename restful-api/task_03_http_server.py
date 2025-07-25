#!/usr/bin/python3
"""
task_O3-http_server.py
"""

import json
import http.server


class API_Server(http.server.BaseHTTPRequestHandler):
    """
    Classe représentant un serveur HTTP simple. Elle hérite de
    BaseHTTPRequestHandler et redéfinit la méthode do_GET pour gérer les
    requêtes GET sur différents endpoints :

    - / : renvoie un message texte "Hello, this is a simple API!"
    - /data : renvoie un dictionnaire encodé en JSON avec des données fictives
    - /status : renvoie "OK" pour indiquer que le serveur est opérationnel
    - /info : renvoie le code HTML
    - Tout autre chemin : renvoie une erreur 404 "Endpoint not found"
    """
    def do_GET(self):
        """
        Gère les requêtes HTTP GET.
        Selon le chemin de la requête (self.path)le serveur renvoie une réponse
        ° 200 : OK ou 404 : Not Found
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, API_Server)
    print(f"Starting server on port {PORT}...")
    httpd.serve_forever()
