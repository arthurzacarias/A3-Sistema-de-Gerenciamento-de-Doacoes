def test_integration_flow(client):
    nova = {
        "nome": "Maria",
        "item": "Água",
        "quantidade": 10
    }
    r1 = client.post("/doacoes", json=nova)
    assert r1.status_code == 201

    r2 = client.get("/doacoes")
    lista = r2.json()
    assert len(lista) >= 1
    assert lista[0]["item"] in ["Água", "Roupas"]
