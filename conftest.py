import pytest


@pytest.fixture
def credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce",
    }


@pytest.fixture
def customer_details():
    return {
        "first_name": "Vishnu",
        "last_name": "AS",
        "postal_code": "345678",
    }
