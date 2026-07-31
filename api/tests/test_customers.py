from fastapi.testclient import TestClient
from ..controllers import customers as controller
from ..main import app
import pytest
from ..models import customers as model

client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_customer(db_session):
    customer_data = {
        "customer_name": "John Doe",
        "email": "john@example.com",
        "phone_number": "555-1234",
        "address": "123 Main Street"
    }

    customer_object = model.Customer(**customer_data)

    created_customer = controller.create(db_session, customer_object)

    assert created_customer is not None
    assert created_customer.customer_name == "John Doe"
    assert created_customer.email == "john@example.com"
    assert created_customer.phone_number == "555-1234"
    assert created_customer.address == "123 Main Street"