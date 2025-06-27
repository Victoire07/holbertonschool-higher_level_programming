#!/usr/bin/python3
"""
Créer la table states dans la base de données passée en argument
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
    Se connecte à la base de données et répertorie tous les objets de l'État
    triés par identifiant par ordre croissant 
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
