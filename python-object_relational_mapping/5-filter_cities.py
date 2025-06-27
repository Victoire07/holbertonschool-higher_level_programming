#!/usr/bin/python3
"""
Afficher les villes d'un état donné(passé en argument)depuis la base de données
hbtn_0e_4_usa, avec protection contre les injections SQL.
Les résultats doivent être affichés sur une seule ligne séparés par des ','
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Print toutes les villes d'un état triées par id
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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    villes_list = cur.fetchall()
    ville_list = [row[0] for row in villes_list]
    print(",".join(ville_list))

    cur.close()
    db.close()
