def test_criar_doacao(client):
    payload = {
        "nome": "Lucas",
        "item": "Roupas",
        "quantidade": 5
    }

    response = client.post("/doacoes", json=payload)
    assert response.status_code == 201
    assert response.json()["nome"] == "Lucas"


def test_listar_doacoes(client):
    response = client.get("/doacoes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
