import sqlite3
from datetime import datetime, timedelta
import pytz
from config.database import get_connection, init_db

def seed_classes():
    db_path = 'fitness_booking.db'
    init_db(db_path)   # <---- ensure tables are created

    conn = get_connection(db_path)
    cursor = conn.cursor()
    tz = pytz.timezone('Asia/Kolkata')

    classes = [
        ('Yoga', tz.localize(datetime.now() + timedelta(days=1)).isoformat(), 'Instructor A', 10),
        ('Zumba', tz.localize(datetime.now() + timedelta(days=2)).isoformat(), 'Instructor B', 15),
        ('HIIT', tz.localize(datetime.now() + timedelta(days=3)).isoformat(), 'Instructor C', 20)
    ]

    cursor.executemany('''
        INSERT INTO classes (name, datetime, instructor, available_slots)
        VALUES (?, ?, ?, ?)
    ''', classes)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    seed_classes()
