# Teste 02 – Verificação de dados retornados pela API ReqRes
import requests

def test_dados_usuario_reqres():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    data = response.json()
    assert data["data"]["id"] == 2
    assert "email" in data["data"]

