import sqlite3
from models.models import create_tables

def get_connection(db_path):
    conn = sqlite3.connect(db_path, check_same_thread=False)
    return conn

def init_db(db_path):
    conn = get_connection(db_path)
    create_tables(conn)
    conn.close()
