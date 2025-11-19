import requests

def buscar_cep(cep: str):
    cep = cep.replace("-", "").strip()

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if "erro" in data:
        return None

    return {
        "logradouro": data.get("logradouro", ""),
        "bairro": data.get("bairro", ""),
        "cidade": data.get("localidade", ""),
        "estado": data.get("uf", "")
    }
