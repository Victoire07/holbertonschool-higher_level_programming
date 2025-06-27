#!/usr/bin/env python3
"""
Afficher tous les états dont le nom commence par un "N" majuscule, triés par id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    """
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
