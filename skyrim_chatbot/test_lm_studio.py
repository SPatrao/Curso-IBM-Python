import requests

def test_lm_studio_connection():
    url = "http://127.0.0.1:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "deepseek-coder-v2-lite-instruct",
        "messages": [
            {"role": "user", "content": "Hola"}
        ]
    }
    
    try:
        # Realizar la solicitud POST
        response = requests.post(url, json=payload, headers=headers)
        
        # Verificar si la respuesta es exitosa
        response.raise_for_status()
        
        # Imprimir la respuesta para asegurarse de que la conexión y el modelo responden bien
        print("Conexión exitosa a LM Studio:")
        print(response.json())  # Aquí puedes ver los datos completos de la respuesta
        
        return True
    
    except requests.exceptions.HTTPError as http_err:
        # Si hay un error de HTTP
        print(f"Error de HTTP al conectar a LM Studio: {http_err}")
        return False
    except requests.exceptions.RequestException as req_err:
        # Si hay otro error de solicitud
        print(f"Error de solicitud al conectar a LM Studio: {req_err}")
        return False
    except Exception as e:
        # Capturar otros errores
        print(f"Error conectando a LM Studio: {e}")
        return False

if __name__ == "__main__":
    test_lm_studio_connection()