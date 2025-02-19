# src/vector_database.py

# Importamos las bibliotecas necesarias para nuestro script
import numpy as np  # Para operaciones numéricas eficientes
import faiss  # Para crear y buscar en índices vectoriales
import pandas as pd  # Para manejar y analizar datos estructurados

# Cargamos los embeddings previamente generados y guardados
# Estos son las representaciones vectoriales de nuestros datos de Skyrim
embeddings = np.load('../data/skyrim_embeddings.npy')

# Cargamos el dataset limpio que contiene la información textual correspondiente a los embeddings
df_clean = pd.read_csv('../data/skyrim_data_clean.csv')

# Inicializamos y configuramos la base de datos vectorial FAISS
# FAISS es una biblioteca para búsqueda eficiente de vectores similares

# Obtenemos la dimensión de nuestros embeddings
# Asumimos que todos los embeddings tienen la misma dimensión
dimension = embeddings.shape[1]

# Creamos un índice FAISS de tipo IndexFlatL2
# Este índice usa la distancia L2 (Euclidiana) para medir la similitud entre vectores
index = faiss.IndexFlatL2(dimension)

# Indexamos los documentos
# Esto añade todos nuestros embeddings al índice FAISS
index.add(embeddings)

# Definimos una función de búsqueda
def search(query_embedding, top_k=5):
    """
    Esta función busca los vectores más similares a un embedding de consulta dado.
    
    Argumentos:
    query_embedding (numpy.ndarray): El embedding de la consulta.
    top_k (int): El número de resultados más similares a devolver.
    
    Retorna:
    list: Una lista de diccionarios, cada uno conteniendo información sobre un resultado similar.
    """
    # Realizamos la búsqueda en el índice FAISS
    # Devuelve las distancias y los índices de los top_k vectores más cercanos
    distances, indices = index.search(np.array([query_embedding]), top_k)
    
    results = []
    # Iteramos sobre los resultados
    for i, idx in enumerate(indices[0]):
        # Creamos un diccionario con la información relevante para cada resultado
        result = {
            'Name': df_clean.iloc[idx]['Name'],
            'Race': df_clean.iloc[idx]['Race'],
            'Gender': df_clean.iloc[idx]['Gender'],
            'Class': df_clean.iloc[idx]['Class'],
            'Distance': distances[0][i]  # La distancia indica qué tan similar es el resultado
        }
        results.append(result)
    
    return results

# Este bloque se ejecuta solo si este script se ejecuta directamente (no si se importa como módulo)
if __name__ == "__main__":
    # Imprimimos información sobre la base de datos vectorial creada
    print(f"Base de datos vectorial creada con {index.ntotal} vectores")
    
    print("Ejemplo de búsqueda:")
    # Realizamos una búsqueda de ejemplo usando el primer embedding de nuestro dataset
    example_results = search(embeddings[0])
    
    # Imprimimos los resultados de la búsqueda de ejemplo
    for result in example_results:
        print(result)

# Notas adicionales:
# - Este script asume que los embeddings en 'skyrim_embeddings.npy' corresponden
#   exactamente a las filas en 'skyrim_data_clean.csv', en el mismo orden.
# - La distancia en los resultados es la distancia Euclidiana. Valores más bajos
#   indican mayor similitud.
# - Este sistema permite búsquedas semánticas eficientes en los datos de Skyrim,
#   encontrando entradas similares basadas en la representación vectorial del texto.