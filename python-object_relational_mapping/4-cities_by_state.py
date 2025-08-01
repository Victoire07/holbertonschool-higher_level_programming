#!/usr/bin/python3
"""
Afficher toutes les villes (cities) avec le nom de leur état (states) associé
depuis la BD hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    Permet d'éxécuter la requête SQL pour afficher toutes les villes
    avec le nom de leur état associé, depuis la base de données hbtn_0e_4_usa
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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC "
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
