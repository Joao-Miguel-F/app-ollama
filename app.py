import requests

def consultar_ollama(prompt):
    url = "http://localhost:11434/api/generate"  # API padrão do Ollama
    payload = {
        "model": "llama3",  # pode trocar por outro modelo instalado no Ollama
        "prompt": prompt
    }

    response = requests.post(url, json=payload, stream=True)

    resposta = ""
    for linha in response.iter_lines():
        if linha:
            dado = linha.decode("utf-8")
            try:
                import json
                dado_json = json.loads(dado)
                if "response" in dado_json:
                    resposta += dado_json["response"]
            except:
                pass

    return resposta


if __name__ == "__main__":
    print("=== Chat com LLM via Ollama ===")
    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Encerrando...")
            break

        resposta = consultar_ollama(user_input)
        print(f"LLM: {resposta}\n")
