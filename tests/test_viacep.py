from unittest.mock import patch
from app.services.viacep import buscar_endereco

@patch("app.services.viacep.requests.get")
def test_buscar_endereco_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"cep": "12345-678"}

    result = buscar_endereco("12345678")
    assert result["cep"] == "12345-678"


@patch("app.services.viacep.requests.get")
def test_buscar_endereco_fail(mock_get):
    mock_get.return_value.status_code = 404
    result = buscar_endereco("99999999")
    assert result is None
