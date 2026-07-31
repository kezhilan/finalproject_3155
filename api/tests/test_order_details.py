from fastapi.testclient import TestClient
from ..controllers import order_details as controller
from ..main import app
import pytest
from ..models import order_details as model


client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order_detail(db_session):
    order_detail_data = {
        "order_id": 1,
        "sandwich_id": 1,
        "amount": 2
    }

    order_detail_object = model.OrderDetail(**order_detail_data)

    created_order_detail = controller.create(db_session, order_detail_object)

    assert created_order_detail is not None
    assert created_order_detail.order_id == 1
    assert created_order_detail.sandwich_id == 1
    assert created_order_detail.amount == 2