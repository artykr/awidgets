from http import HTTPStatus

from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from awidgets import models
from awidgets.main import app
from tests.utils import generate_random_widget, remove_all_widgets

client = TestClient(app)


def test_create_widget(db_session: Session):
    response = client.post(
        "/widgets/",
        json={"name": "Test Widget", "number_of_parts": 10},
    )

    assert response.status_code == HTTPStatus.CREATED
    data = response.json()
    assert data["name"] == "Test Widget"
    assert data["number_of_parts"] == 10

    remove_all_widgets(db_session)


def test_get_widget(db_session: Session):
    widget = generate_random_widget(db_session)
    response = client.get(f"/widgets/{widget.id}")

    assert response.status_code == HTTPStatus.OK

    content = response.json()

    assert content["name"] == widget.name
    assert content["number_of_parts"] == widget.number_of_parts
    assert content["id"] == widget.id

    remove_all_widgets(db_session)


def test_get_widgets(db_session: Session):
    widget1 = generate_random_widget(db_session)
    widget1_data = jsonable_encoder(widget1)

    widget2 = generate_random_widget(db_session)
    widget2_data = jsonable_encoder(widget2)

    response = client.get("/widgets/")

    assert response.status_code == HTTPStatus.OK

    content = response.json()

    assert len(content) == 2

    assert content == [
        {
            "name": widget1_data["name"],
            "number_of_parts": widget1_data["number_of_parts"],
            "id": widget1_data["id"],
            "created_date": widget1_data["created_date"],
            "updated_date": widget1_data["updated_date"],
        },
        {
            "name": widget2_data["name"],
            "number_of_parts": widget2_data["number_of_parts"],
            "id": widget2_data["id"],
            "created_date": widget2_data["created_date"],
            "updated_date": widget2_data["updated_date"],
        },
    ]

    remove_all_widgets(db_session)


def test_update_widget(db_session: Session):
    widget = generate_random_widget(db_session)

    response = client.put(
        f"/widgets/{widget.id}",
        json={"name": "Test Widget Updated", "number_of_parts": 101},
    )

    assert response.status_code == HTTPStatus.OK

    content = response.json()

    assert content["name"] == "Test Widget Updated"
    assert content["number_of_parts"] == 101
    assert content["id"] == widget.id

    remove_all_widgets(db_session)


def test_delete_widget(db_session: Session):
    widget = generate_random_widget(db_session)

    response = client.delete(f"/widgets/{widget.id}")
    assert response.status_code == HTTPStatus.NO_CONTENT

    result = (
        db_session.query(models.Widget).filter(models.Widget.id == widget.id).first()
    )
    assert result is None
