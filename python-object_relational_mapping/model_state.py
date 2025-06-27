#!/usr/bin/python3
"""
Définit une classe State qui fait référence à la table states de MySQL
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()
class State(Base):
    """
    Classe représentant l'état dans la base de données
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

