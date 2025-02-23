import pandas as pd
from BD_clases import Collection

df_personajes = pd.read_csv("data/Skyrim_Named_Characters_Propio.csv")
df_libros = pd.read_csv("data/skyrim_books.csv")

db = Collection()

for _, row in df_personajes.iterrows():
    db.add_personaje(row["Name"], row["Home City"], row["Health (PC=10)"], row["Magicka (PC=10)"], row["Stamina (PC=10)"])
    print(f"Personaje insertado: {row['Name']}")

for _, row in df_libros.iterrows():
    db.add_libro(row["Title"], row["Cost"], row["Author"], row["Description"], row["Skill"])
    print(f"Libro insertado: {row['Title']}")
