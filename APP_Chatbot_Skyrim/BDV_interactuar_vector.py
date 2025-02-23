from langchain_chroma import Chroma  # Usar la versión actualizada
from langchain_huggingface import HuggingFaceEmbeddings

# Ruta a la base de datos persistente de Chroma
persist_directory = "db"  # La carpeta donde guardaste la base de datos

# Definir la función de embeddings
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def cargar_db_vectorial():
    try:
        # Cargar la base de datos Chroma desde la carpeta persistente, incluyendo la función de embeddings
        db = Chroma(persist_directory="db", collection_name="skyrim-combined", embedding_function=embedding_function)
        return db
    except Exception as e:
        print(f"Error al cargar la base de datos vectorial: {e}")
        return None

def buscar_similitud(db, query, top_k=5):
    try:
        # Realizar la búsqueda de similitud
        results = db.similarity_search(query, k=top_k)
        return results
    except Exception as e:
        print(f"Error durante la búsqueda de similitud: {e}")
        return []

def buscar_similitud_con_score(db, query, top_k=5):
    try:
        # Realizar la búsqueda de similitud con puntuaciones
        results = db.similarity_search_with_score(query, k=top_k)
        return results
    except Exception as e:
        print(f"Error durante la búsqueda de similitud: {e}")
        return []

if __name__ == "__main__":
    db = cargar_db_vectorial()
    if db:
        # Solicitar al usuario qué tipo de búsqueda desea realizar
        opcion = input("Elige el tipo de búsqueda (1: Similitud simple, 2: Similitud con puntuación): ")

        # Realizar la búsqueda de acuerdo a la opción seleccionada
        if opcion == "1":
            query = input("Introduce tu consulta para similarity_search: ")
            results = buscar_similitud(db, query)
            
            # Mostrar los resultados de similarity_search
            if results:
                print(f"Se encontraron {len(results)} resultados para la consulta '{query}':")
                for i, result in enumerate(results):
                    print(f"Resultado {i+1}: {result.page_content}")
            else:
                print("No se encontraron resultados.")
        
        elif opcion == "2":
            query = input("Introduce tu consulta para similarity_search_with_score: ")
            results = buscar_similitud_con_score(db, query)

            # Mostrar los resultados de similarity_search_with_score
            if results:
                print(f"Se encontraron {len(results)} resultados para la consulta '{query}':")
                for i, (result, score) in enumerate(results):
                    print(f"Resultado {i+1}: {result.page_content} (Score: {score})")
            else:
                print("No se encontraron resultados.")
        
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")
