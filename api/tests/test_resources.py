from fastapi.testclient import TestClient
from ..controllers import resources as controller
from ..main import app
import pytest
from ..models import resources as model


client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_resource(db_session):
    resource_data = {
        "item": "Bread",
        "amount": 100,
        "unit": "Slices"
    }

    resource_object = model.Resource(**resource_data)

    created_resource = controller.create(db_session, resource_object)

    assert created_resource is not None
    assert created_resource.item == "Bread"
    assert created_resource.amount == 100
    assert created_resource.unit == "Slices"