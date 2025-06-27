#!/usr/bin/env python3

"""
Afficher tous les enregistrements de la table states, triés par id croissant,
à partir de la base de données passée en argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Afficher tous les enregistrements de la table states triés par id croissant
    à partir de la base de données passée en argument.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
