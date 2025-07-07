# models.py

import sqlite3

def create_tables(conn):
    cursor = conn.cursor()
    # Table for fitness classes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            datetime TEXT NOT NULL,
            instructor TEXT NOT NULL,
            available_slots INTEGER NOT NULL
        )
    ''')

    # Table for bookings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class_id INTEGER NOT NULL,
            client_name TEXT NOT NULL,
            client_email TEXT NOT NULL,
            booked_at TEXT NOT NULL,
            FOREIGN KEY (class_id) REFERENCES classes (id)
        )
    ''')

    conn.commit()
