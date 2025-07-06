from APItests.tests.client.client import client
from APItests.tests.registration.data_registrartion import generate_user_registration
from data_exist import generate_user_exist_unregistered

def test_exist_registered_user(client, generate_user_registration):
    register_response = client.register_user(generate_user_registration)
    user = {k: generate_user_registration[k] for k in ["email"]}
    exist_response = client.exist_user(user)
    data = exist_response.json()
    assert exist_response.status_code == 200, "Статус код должен быть равен 200"
    assert data['exist'] == True, "Значение поля exist в response должно быть равно True"

def test_exist_unregistered_user(client, generate_user_exist_unregistered):
    response = client.exist_user(generate_user_exist_unregistered)
    data = response.json()
    assert response.status_code == 200, "Статус код должен быть равен 200"
    assert data['exist'] == False, "Значение поля exist в response должно быть равно False"