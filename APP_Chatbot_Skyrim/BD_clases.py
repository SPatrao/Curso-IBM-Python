import sqlite3
import os

class Collection:
    def __init__(self, db_path="data/skyrim_data.db"):
        self.db_path = db_path
        # Crear la carpeta data si no existe
        if not os.path.exists(os.path.dirname(self.db_path)):
            os.makedirs(os.path.dirname(self.db_path))

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        # Crear tablas si no existen
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                home_city TEXT,
                health INTEGER,
                magicka INTEGER,
                stamina INTEGER
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS libros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                cost INTEGER,
                author TEXT,
                description TEXT,
                skill TEXT
            );
        ''')

    def add_personaje(self, name, home_city, health, magicka, stamina):
        self.cursor.execute('''
            INSERT INTO personajes (name, home_city, health, magicka, stamina)
            VALUES (?, ?, ?, ?, ?);
        ''', (name, home_city, health, magicka, stamina))
        self.conn.commit()

    def add_libro(self, title, cost, author, description, skill):
        self.cursor.execute('''
            INSERT INTO libros (title, cost, author, description, skill)
            VALUES (?, ?, ?, ?, ?);
        ''', (title, cost, author, description, skill))
        self.conn.commit()

    def __del__(self):
        self.conn.close()