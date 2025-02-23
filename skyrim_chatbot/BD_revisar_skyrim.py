import sqlite3

# Definir la ruta a la base de datos
DB_PATH = "data/skyrim_data.db"  # Ruta correcta de tu archivo de base de datos

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Verificar las tablas existentes en la base de datos
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("🔹 Tablas en la base de datos:", tables)

# Verificar el número de personajes en la base de datos
cursor.execute("SELECT COUNT(*) FROM personajes")
print(f"🔹 Personajes en la base de datos: {cursor.fetchone()[0]}")

# Verificar el número de libros en la base de datos
cursor.execute("SELECT COUNT(*) FROM libros")
print(f"🔹 Libros en la base de datos: {cursor.fetchone()[0]}")

# Ver los primeros 5 personajes
cursor.execute("SELECT * FROM personajes LIMIT 5;")
print("🔹 Ejemplo de personajes:", cursor.fetchall())

# Ver los primeros 5 libros
cursor.execute("SELECT * FROM libros LIMIT 5;")
print("🔹 Ejemplo de libros:", cursor.fetchall())

conn.close()
