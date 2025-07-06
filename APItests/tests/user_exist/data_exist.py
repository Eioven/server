import pytest
from faker import Faker

fake = Faker()

@pytest.fixture
def generate_user_exist_unregistered():
    return {
    'email': fake.email(),
    }
