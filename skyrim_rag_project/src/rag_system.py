# src/rag_system.py

from vector_database import search
from response_generator import generate_response

def rag_query(query, top_k=3):
    """
    Realiza una consulta RAG completa: busca información relevante y genera una respuesta.
    
    :param query: La consulta del usuario
    :param top_k: Número de resultados de búsqueda a considerar
    :return: Respuesta generada
    """
    # Realizar búsqueda
    search_results = search(query, top_k)
    
    # Preparar contexto para la generación de respuesta
    context = "\n".join([f"{result['Name']} - {result['Race']} {result['Class']} with skills in {result['Primary Skills']}" 
                         for result in search_results])
    
    # Generar respuesta
    response = generate_response(query, context)
    
    return response

if __name__ == "__main__":
    # Ejemplo de uso
    query = "Tell me about Nord warriors with two-handed skills"
    response = rag_query(query)
    print(f"Query: {query}")
    print(f"Generated Response: {response}")

