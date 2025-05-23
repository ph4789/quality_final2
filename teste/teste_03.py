# Teste 03 – Simulação de criação de usuário com POST
import requests

def test_criar_usuario_reqres():
    url = "https://reqres.in/api/users"
    payload = {
        "name": "Pedro",
        "job": "QA Tester"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Pedro"
