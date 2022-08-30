import datetime

from pydantic import BaseModel


class WidgetBase(BaseModel):
    name: str
    number_of_parts: int


class WidgetCreate(WidgetBase):
    pass


class WidgetUpdate(WidgetBase):
    pass


class Widget(WidgetBase):
    id: int
    created_date: datetime.date
    updated_date: datetime.date

    class Config:
        orm_mode = True
