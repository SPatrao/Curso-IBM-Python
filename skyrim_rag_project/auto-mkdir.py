import os

# Crear la estructura de carpetas
os.makedirs('skyrim_rag_project/data', exist_ok=True)
os.makedirs('skyrim_rag_project/src', exist_ok=True)
os.makedirs('skyrim_rag_project/models', exist_ok=True)

# Crear archivos vacíos
open('skyrim_rag_project/src/data_processing.py', 'a').close()
open('skyrim_rag_project/src/vector_database.py', 'a').close()
open('skyrim_rag_project/src/main.py', 'a').close()
open('skyrim_rag_project/requirements.txt', 'a').close()
open('skyrim_rag_project/README.md', 'a').close()

# Crear el archivo embedding_generation.py con el contenido
with open('skyrim_rag_project/src/embedding_generation.py', 'w') as f:
    f.write('''# src/embedding_generation.py'''

print("Estructura de carpetas y archivos creada con éxito.")

