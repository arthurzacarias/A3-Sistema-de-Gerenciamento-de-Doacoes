def test_root_should_return_homepage(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "html" in response.text.lower()
