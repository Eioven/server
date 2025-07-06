import pytest
from APItests.tests.registration.data_registrartion import generate_user_registration
from APItests.tests.client.client import client
from data_test_login import data_test_login_negative

def test_login_registered_user(client, generate_user_registration):
  register_response = client.register_user(generate_user_registration)
  user = {k: generate_user_registration[k] for k in ["email", "password"]}
  login_response = client.login_user(user)
  assert login_response.status_code == 200, "Статус код должен быть равен 200"


@pytest.mark.parametrize('data', data_test_login_negative)
def test_login_negative(client, data):
  response = client.login_user(data)
  assert response.status_code == 422, "Статус код должен быть равен 422"

