#!/usr/bin/python3
"""
Script sécurisé contre les injections SQL
Affiche les états dont le nom correspond à celui donné par l'utilisateur
(4e argument), depuis la base de données spécifiée.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Exécution principale du script :
    Connexion à la base de données et affichage des états
    correspondant exactement au nom fourni par l'utilisateur
    (via le 4e argument de la ligne de commande).
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE name = %s "
        "ORDER BY id ASC",
        (sys.argv[4],)
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
