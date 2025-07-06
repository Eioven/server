from APItests.tests.client.client import client
from APItests.tests.registration.data_registrartion import generate_user_registration
from data_name_edit import generate_name, empty_name, generate_token


def test_name_edit_user_valid_token(client, generate_user_registration, generate_name):
    register_response = client.register_user(generate_user_registration)
    token = register_response.json()['token']
    client.update_headers({'Authorization': f'Bearer {token}'})
    edit_response = client.name_edit_user(generate_name)
    assert edit_response.status_code == 200, "Статус код должен быть равен 200"

def test_name_edit_user_invalid_token(client, generate_name,generate_token):
    token = generate_token
    client.update_headers({'Authorization': f'Bearer {token}'})
    response = client.name_edit_user(generate_name)
    assert response.status_code == 401, "Статус код должен быть равен 401"

def test_name_edit_user_validation_error(client, generate_user_registration, empty_name):
    register_response = client.register_user(generate_user_registration)
    token = register_response.json()['token']
    client.update_headers({'Authorization': f'Bearer {token}'})
    edit_response = client.name_edit_user(empty_name)
    assert edit_response.status_code == 422, "Статус код должен быть равен 422"