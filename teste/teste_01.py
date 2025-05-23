# Teste 01 – Verificação de status da API ReqRes
import requests

def test_status_api_reqres():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    assert response.status_code == 200
