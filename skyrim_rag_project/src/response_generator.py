# src/response_generator.py

import requests
import json

# URL de la API local de LMStudio (ajusta esto según tu configuración)
LM_STUDIO_API_URL = "http://localhost:1234/v1/chat/completions"

def generate_response(query, context):
    """
    Genera una respuesta basada en la consulta y el contexto proporcionados,
    utilizando un modelo local a través de LMStudio.
    
    :param query: La consulta del usuario
    :param context: Información relevante recuperada de la base de datos
    :return: Respuesta generada
    """
    prompt = f"Query: {query}\nContext: {context}\nResponse:"
    
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant with knowledge about Skyrim."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }
    
    try:
        response = requests.post(LM_STUDIO_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except requests.RequestException as e:
        print(f"Error al generar respuesta: {e}")
        return "Lo siento, no pude generar una respuesta en este momento."

if __name__ == "__main__":
    # Ejemplo de uso
    query = "Tell me about Nord warriors with two-handed skills"
    context = "Nord warriors often specialize in two-handed weapons. They are known for their strength and combat prowess. Some notable Nord warriors include Ragnar, who has skills in Smithing and Two-handed combat."
    
    response = generate_response(query, context)
    print(f"Query: {query}")
    print(f"Context: {context}")
    print(f"Generated Response: {response}")