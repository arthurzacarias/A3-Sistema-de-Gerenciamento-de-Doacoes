from unittest.mock import patch

@patch("app.services.viacep.requests.get")
def test_cep_valid(mock_get, client):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "cep": "12345-000",
        "localidade": "Cidade Teste",
        "uf": "TS",
        "logradouro": "Rua Teste"
    }

    response = client.get("/cep/12345000")
    assert response.status_code == 200
    data = response.json()
    assert data["localidade"] == "Cidade Teste"
    assert data["uf"] == "TS"


@patch("app.services.viacep.requests.get")
def test_cep_error(mock_get, client):
    mock_get.return_value.status_code = 400
    response = client.get("/cep/00000000")
    assert response.status_code == 400
