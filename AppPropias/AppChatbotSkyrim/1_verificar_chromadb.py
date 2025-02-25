from langchain_community.vectorstores.chroma import Chroma

DB_DIR = "chroma"  # Cambia esto si usaste otro nombre

db = Chroma(persist_directory=DB_DIR, collection_name="skyrim-combined")
print("🔹 Número de documentos en la base de datos vectorial:", db._collection.count())
