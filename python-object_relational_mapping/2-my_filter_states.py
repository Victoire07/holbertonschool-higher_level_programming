#!/usr/bin/python3
"""
Afficher uniquement la ligne correspondant à l'état dont le nom est fourni
par l'utilisateur dans le terminal
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Afficher uniquement la ligne correspondant à l'état dont le nom est fourni
    par l'utilisateur dans le terminal
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = '{}' "
        "ORDER BY id ASC"
        ).format(sys.argv[4])

    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
