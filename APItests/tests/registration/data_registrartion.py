import pytest
from faker import Faker

fake = Faker()

@pytest.fixture
def generate_user_registration():
  return {
    "email": fake.email(),
    "password": fake.password(),
    "age": fake.random_int(min=0, max=99)
  }