from fastapi.testclient import TestClient
from ..controllers import promotions as controller
from ..main import app
import pytest
from ..models import promotions as model
from datetime import datetime


client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promotion(db_session):
    promotion_data = {
        "promotion_code": "Half",
        "expiration_date": datetime(2026, 12, 31)
    }

    promotion_object = model.Promotion(**promotion_data)

    created_promotion = controller.create(db_session, promotion_object)

    assert created_promotion is not None
    assert created_promotion.promotion_code == "Half"
    assert created_promotion.expiration_date == datetime(2026, 12, 31)