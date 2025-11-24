def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    # Verifica se o template renderizou algo esperado (ex: título ou tabela)
    # Obs: Isso depende do seu index.html ter esse conteúdo
    # assert "Doações" in response.text

def test_cadastro_page(client):
    response = client.get("/cadastro")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_confirmacao_page(client):
    # A página de confirmação espera query params
    response = client.get("/confirmacao?item=Teste&quantidade=1&tipo=Doacao")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]