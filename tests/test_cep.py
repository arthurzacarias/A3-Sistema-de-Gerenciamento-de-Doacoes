from unittest.mock import patch

# O prefixo definido em cep.py é "/api"
def test_cep_endpoint_valid(client):
    # Mockamos a função buscar_cep para não chamar a API real
    with patch("app.routers.cep.buscar_cep") as mock_busca:
        mock_busca.return_value = {
            "logradouro": "Rua Teste",
            "bairro": "Bairro Teste",
            "cidade": "Cidade Teste",
            "estado": "TS"
        }
        
        # A URL correta agora é /api/cep/{cep}
        response = client.get("/api/cep/12345000")
        
        assert response.status_code == 200
        data = response.json()
        assert data["logradouro"] == "Rua Teste"
        assert data["estado"] == "TS"

def test_cep_endpoint_invalid(client):
    with patch("app.routers.cep.buscar_cep") as mock_busca:
        mock_busca.return_value = None
        
        response = client.get("/api/cep/00000000")
        
        assert response.status_code == 200
        assert response.json() == {"erro": "CEP inválido"}