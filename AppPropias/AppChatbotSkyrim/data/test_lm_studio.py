# test_lm_studio.py
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
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print("Conexión exitosa a LM Studio:")
        print(response.json())
        return True
    except Exception as e:
        print(f"Error conectando a LM Studio: {e}")
        return False

if __name__ == "__main__":
    test_lm_studio_connection()
