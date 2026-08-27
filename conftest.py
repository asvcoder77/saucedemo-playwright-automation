import os

import pytest


@pytest.fixture


def credentials():
    return {
        "username": os.getenv("TEST_USERNAME", "standard_user"),
        "password": os.getenv("TEST_PASSWORD", "secret_sauce"),
    }


@pytest.fixture
def customer_details():
    return {
        "first_name": "Vishnu",
        "last_name": "AS",
        "postal_code": "345678",
    }
