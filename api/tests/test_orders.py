from fastapi.testclient import TestClient
from ..controllers import orders as controller
from ..main import app
import pytest
from ..models import orders as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order(db_session):
    # Create a sample order
    order_data = {
        "customer_id": 1,
        "tracking_number": "100",
        "order_status": "Pending",
        "total_price": 15.99,
        "description": "Lunch order",
        "promotion_id": 1
    }

    order_object = model.Order(**order_data)

    # Call the create function
    created_order = controller.create(db_session, order_object)

    # Assertions
    assert created_order is not None
    assert created_order.customer_id == 1
    assert created_order.tracking_number == "100"
    assert created_order.order_status == "Pending"
    assert created_order.total_price == 15.99
    assert created_order.description == "Lunch order"
    assert created_order.promotion_id == 1