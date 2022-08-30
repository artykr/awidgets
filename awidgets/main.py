from http import HTTPStatus
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import Response
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from awidgets import schemas
from awidgets.core.constants import CORS_ORIGINS, PROJECT_NAME
from awidgets.repositories import widgets_repository
from awidgets.services.db import get_db_session

app = FastAPI(title=PROJECT_NAME)

if CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.post("/widgets/", response_model=schemas.Widget, status_code=HTTPStatus.CREATED)
def create_widget(
    widget: schemas.WidgetCreate, db_session: Session = Depends(get_db_session)
):
    return widgets_repository.create_widget(db_session=db_session, widget=widget)


@app.get("/widgets/", response_model=List[schemas.Widget])
def read_widgets(
    response: Response,
    skip: int = 0,
    limit: int = 100,
    db_session: Session = Depends(get_db_session),
):
    widgets = widgets_repository.get_widgets(db_session, skip=skip, limit=limit)
    response.headers["X-Total-Count"] = str(
        widgets_repository.get_widgets_count(db_session)
    )

    return widgets


@app.get("/widgets/{widget_id}", response_model=schemas.Widget)
def read_widget(widget_id: int, db_session: Session = Depends(get_db_session)):
    widget = widgets_repository.get_widget(db_session, widget_id=widget_id)
    if widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")

    return widget


@app.delete("/widgets/{widget_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_widget(widget_id: int, db_session: Session = Depends(get_db_session)):
    widget = widgets_repository.delete_widget(db_session, widget_id=widget_id)

    if widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")


@app.put("/widgets/{widget_id}", response_model=schemas.Widget)
def update_widget(
    widget_id: int,
    widget: schemas.WidgetUpdate,
    db_session: Session = Depends(get_db_session),
):
    updated_widget = widgets_repository.update_widget(
        db_session, widget_id=widget_id, widget=widget
    )

    if updated_widget is None:
        raise HTTPException(status_code=404, detail="Widget not found")

    return updated_widget
