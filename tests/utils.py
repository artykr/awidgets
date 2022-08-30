import random

from sqlalchemy.orm import Session

from awidgets import models

MIN_NUMBER_OF_PARTS = 1
MAX_NUMBER_OF_PARTS = 100


def generate_random_widget(db_session: Session) -> models.Widget:
    widget_number = random.randint(MIN_NUMBER_OF_PARTS, MAX_NUMBER_OF_PARTS)

    new_widget = models.Widget(
        name=f"Test Widget Number {widget_number}", number_of_parts=widget_number
    )

    db_session.add(new_widget)
    db_session.commit()
    db_session.refresh(new_widget)

    return new_widget


def remove_all_widgets(db_session: Session):
    db_session.query(models.Widget).delete()
    db_session.commit()
