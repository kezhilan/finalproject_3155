from fastapi.testclient import TestClient
from ..controllers import sandwiches as controller
from ..main import app
import pytest
from ..models import sandwiches as model


client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_sandwich(db_session):
    sandwich_data = {
        "sandwich_name": "Classic Chicken",
        "price": 8.99,
        "calories": 650,
        "category": "Lunch"
    }

    sandwich_object = model.Sandwich(**sandwich_data)

    created_sandwich = controller.create(db_session, sandwich_object)

    assert created_sandwich is not None
    assert created_sandwich.sandwich_name == "Classic Chicken"
    assert created_sandwich.price == 8.99
    assert created_sandwich.calories == 650
    assert created_sandwich.category == "Lunch"