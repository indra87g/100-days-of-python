import sqlite3 as sq


def create_connection():
    return sq.connect("app.db")


def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
              )"""
    )
    conn.commit()
    conn.close()
