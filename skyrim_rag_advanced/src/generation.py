import requests

def generate_response(prompt, api_url="http://localhost:1234/v1/completions"):
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "deepseek-coder-v2-lite-instruct",
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7,
        "top_p": 0.95,
        "stop": ["\n\nHuman:", "\n\nAssistant:"]
    }
    response = requests.post(api_url, headers=headers, json=data)
    return response.json()['choices'][0]['text'].strip()

def generate_prompt(query, results):
    context = "\n".join(results['text'].tolist())
    return f"Query: {query}\nContext:\n{context}\nAnswer:"

if __name__ == '__main__':
    query = "Tell me about Nord warriors"
    context = "Nord: Warrior race from Skyrim. Skills: Two-handed, Heavy Armor."
    prompt = generate_prompt(query, pd.DataFrame({'text': [context]}))
    response = generate_response(prompt)
    print(response)

