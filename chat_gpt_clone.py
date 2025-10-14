from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()



# Para conversación interactiva:
def interactive_chat():
    api_key = os.getenv("MISTRAL_API_KEY")
    
    print("Chat con Mistral AI - Modelo: mistral-tiny")
    print("Escribe tu mensaje (o 'quit', 'exit', 'salir' para terminar chat.):")
    
    while True:
        user_input = input("\n👤 Usuario: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'salir']:
            break
            
        if not user_input:
            continue
            
        # Solicitud IDÉNTICA a la documentación
        response = requests.post(
            "https://api.mistral.ai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mistral-tiny",
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }
        )
        
        if response.status_code == 200:
            result = response.json()
            assistant_message = result["choices"][0]["message"]["content"]
            print(f"🤖 Assistant: {assistant_message}")
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    interactive_chat()