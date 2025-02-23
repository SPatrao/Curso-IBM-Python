import streamlit as st
import requests
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from BDV_interactuar_vector import cargar_db_vectorial

# 🔹 Configuración de la base de datos vectorial
persist_directory = "db"
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory=persist_directory, collection_name="skyrim-combined", embedding_function=embedding_function)

def verificar_datos(db):
    try:
        # Obtener los IDs de todos los documentos almacenados
        docs = db.get()
        print(f"Total de documentos en la BD: {len(docs['ids'])}")

        # Mostrar las primeras 5 entradas
        for i in range(min(5, len(docs['ids']))):
            print(f"Documento {i+1}: {docs['documents'][i]}")
    except Exception as e:
        print(f"Error al verificar datos en la BD: {e}")

if __name__ == "__main__":
    db = cargar_db_vectorial()
    if db:
        verificar_datos(db)

