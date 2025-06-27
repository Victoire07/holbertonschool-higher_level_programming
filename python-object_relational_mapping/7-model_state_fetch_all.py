#!/usr/bin/env python3
"""
Liste tous les objets State de la base hbtn_0e_6_usa, triés par id.
Affiche : <id>: <name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State 

