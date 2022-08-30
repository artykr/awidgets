from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from awidgets import models, schemas
from awidgets.core.constants import DEFAULT_LIST_RESPONSE_LIMIT


def get_widget(db_session: Session, widget_id: int) -> Optional[models.Widget]:
    return db_session.query(models.Widget).filter(models.Widget.id == widget_id).first()


def get_widgets(
    db_session: Session, skip: int = 0, limit: int = DEFAULT_LIST_RESPONSE_LIMIT
) -> List[models.Widget]:
    return (
        db_session.query(models.Widget)
        .order_by(models.Widget.id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def get_widgets_count(db_session: Session) -> int:
    return db_session.query(models.Widget).count()


def create_widget(db_session: Session, widget: schemas.WidgetCreate) -> models.Widget:
    new_widget = models.Widget(**widget.dict())

    db_session.add(new_widget)
    db_session.commit()
    db_session.refresh(new_widget)

    return new_widget


def delete_widget(db_session: Session, widget_id: int) -> Optional[models.Widget]:
    widget = (
        db_session.query(models.Widget).filter(models.Widget.id == widget_id).first()
    )

    if widget is None:
        return None

    db_session.delete(widget)
    db_session.commit()

    return widget


def update_widget(
    db_session: Session, widget_id: int, widget: schemas.WidgetUpdate
) -> Optional[models.Widget]:
    existing_widget = (
        db_session.query(models.Widget).filter(models.Widget.id == widget_id).first()
    )

    if existing_widget is None:
        return None

    existing_widget_data = jsonable_encoder(existing_widget)
    new_widget_data = widget.dict(exclude_unset=True)

    for field in existing_widget_data:
        if field in new_widget_data:
            setattr(existing_widget, field, new_widget_data[field])

    db_session.add(existing_widget)
    db_session.commit()
    db_session.refresh(existing_widget)

    return existing_widget
