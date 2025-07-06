import pytest
from faker import Faker

faker = Faker()

@pytest.fixture
def generate_name():
    return {
        "name": faker.name()
    }

@pytest.fixture
def empty_name():
    return {
        "name": ""
    }

@pytest.fixture
def generate_token():
    return faker.windows_platform_token()