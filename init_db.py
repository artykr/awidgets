import random
from typing import List

from awidgets import models
from awidgets.services.db import SessionLocal

NUMBER_OF_WIDGETS = 5
MIN_NUMBER_OF_PARTS = 2
MAX_NUMBER_OF_PARTS = 10


def init_db():
    db_session = SessionLocal()
    widgets = generate_widgets()

    db_session.bulk_save_objects(widgets)
    db_session.commit()


def generate_widgets() -> List[models.Widget]:
    widgets = []
    for widget_number in range(NUMBER_OF_WIDGETS):
        widget = models.Widget(
            name=f"My Awesome Widget {widget_number}",
            number_of_parts=random.randint(MIN_NUMBER_OF_PARTS, MAX_NUMBER_OF_PARTS),
        )
        widgets.append(widget)

    return widgets


if __name__ == "__main__":
    init_db()
