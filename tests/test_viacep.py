from unittest.mock import patch
from app.services.viacep import buscar_cep

@patch("app.services.viacep.requests.get")
def test_buscar_cep_success(mock_get):
    # Simula o JSON cru que o ViaCEP retorna
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "cep": "01001-000",
        "logradouro": "Praça da Sé",
        "complemento": "lado ímpar",
        "bairro": "Sé",
        "localidade": "São Paulo",
        "uf": "SP",
        "ibge": "3550308",
        "gia": "1004",
        "ddd": "11",
        "siafi": "7107"
    }

    # Executa sua função
    result = buscar_cep("01001000")

    # Verifica se sua função filtrou os campos corretamente conforme viacep.py
    assert result is not None
    assert result["logradouro"] == "Praça da Sé"
    assert result["cidade"] == "São Paulo" # viacep.py mapeia localidade -> cidade
    assert result["estado"] == "SP"

@patch("app.services.viacep.requests.get")
def test_buscar_cep_error(mock_get):
    # Simula erro da API (ex: CEP inexistente retorna erro: true no JSON)
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"erro": True}

    result = buscar_cep("99999999")
    assert result is None