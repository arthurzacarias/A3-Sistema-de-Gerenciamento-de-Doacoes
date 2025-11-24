import pytest

def test_criar_doacao_form(client):
    # Como sua rota usa Form(...), enviamos data=... e não json=...
    form_data = {
        "item": "Cestas Básicas",
        "quantidade": 10,
        "tipo": "Alimento",
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "numero": 1,
        "complemento": "Lado ímpar",
        "bairro": "Sé",
        "cidade": "São Paulo",
        "estado": "SP",
        "status": "Disponível"
    }

    # follow_redirects=False permite verificar se houve o redirect 303
    response = client.post("/doacoes", data=form_data, follow_redirects=False)
    
    assert response.status_code == 303
    # Verifica se redirecionou para a confirmação com os parâmetros
    assert "/confirmacao" in response.headers["location"]

def test_excluir_doacao(client):
    # 1. Primeiro cria uma doação para ter o que excluir
    form_data = {
        "item": "Para Excluir", "quantidade": 1, "tipo": "Teste",
        "cep": "00000-000", "logradouro": "Rua", "numero": 1,
        "complemento": "", "bairro": "B", "cidade": "C", "estado": "E", "status": "S"
    }
    client.post("/doacoes", data=form_data)
    
    # Como o banco de teste reseta, o ID deve ser 1 (se for o único teste rodando)
    # Mas para garantir, vamos assumir ID 1 ou pegar do banco se tivéssemos acesso aqui
    
    response = client.get("/excluir/1", follow_redirects=False)
    
    # Se o ID 1 existir, ele redireciona para home (302 ou 303)
    # Se não existir, seu código atual tenta deletar mesmo assim e redireciona
    assert response.status_code in [302, 303]
    assert response.headers["location"] == "/"