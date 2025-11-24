def test_editar_doacao_flow(client):
    # 1. Cria doação inicial para ter o que editar
    dados_originais = {
        "item": "Cadeira Velha", "quantidade": 1, "tipo": "Móvel",
        "cep": "00000-000", "logradouro": "Rua A", "numero": 10,
        "complemento": "", "bairro": "Bairro A", "cidade": "Cidade A",
        "estado": "AA", "status": "Velho"
    }
    client.post("/doacoes", data=dados_originais)

    # 2. Acessa a página de edição (GET)
    response_get = client.get("/editar/1")
    assert response_get.status_code == 200
    assert "Cadeira Velha" in response_get.text

    # 3. Envia a edição (POST) com TODOS os campos exigidos pelo router novo
    dados_editados = {
        "item": "Cadeira Nova",
        "quantidade": 2,
        "tipo": "Móvel Reformado",
        "cep": "11111-111", 
        "logradouro": "Rua Nova",
        "numero": 20,
        "complemento": "Apto 1",
        "bairro": "Bairro Novo", 
        "cidade": "Cidade Nova", 
        "estado": "BB",
        "status": "Novo"
    }
    
    # O router doacoes.py retorna 303 (See Other), não 302
    response_post = client.post("/editar/1", data=dados_editados, follow_redirects=False)
    
    assert response_post.status_code == 303
    assert response_post.headers["location"] == "/"

    # 4. Verifica na home se o texto mudou
    response_home = client.get("/")
    assert "Cadeira Nova" in response_home.text

def test_excluir_doacao_flow(client):
    # 1. Cria doação
    dados = {
        "item": "Lixo Eletrônico", "quantidade": 5, "tipo": "Sucata",
        "cep": "11111-111", "logradouro": "Rua L", "numero": 9,
        "complemento": "", "bairro": "B", "cidade": "C", "estado": "E", "status": "S"
    }
    client.post("/doacoes", data=dados)

    # 2. Exclui (GET /excluir/{id})
    response = client.get("/excluir/1", follow_redirects=False)
    
    # Assert corrigido para esperar 303
    assert response.status_code == 303
    assert response.headers["location"] == "/"
    
    # 3. Verifica se sumiu da home
    response_home = client.get("/")
    assert "Lixo Eletrônico" not in response_home.text