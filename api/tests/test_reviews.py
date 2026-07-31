from fastapi.testclient import TestClient
from ..controllers import reviews as controller
from ..main import app
import pytest
from ..models import reviews as model


client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_review(db_session):
    review_data = {
        "customer_id": 1,
        "sandwich_id": 1,
        "review_text": "Excellent sandwich!",
        "rating": 5
    }

    review_object = model.Review(**review_data)

    created_review = controller.create(db_session, review_object)

    assert created_review is not None
    assert created_review.customer_id == 1
    assert created_review.sandwich_id == 1
    assert created_review.review_text == "Excellent sandwich!"
    assert created_review.rating == 5