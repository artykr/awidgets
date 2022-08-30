from sqlalchemy import Column, Date, Integer, String, func

from awidgets.models.base import Base


class Widget(Base):
    __tablename__ = "widgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
    number_of_parts = Column(Integer)
    created_date = Column(Date, server_default=func.current_date())
    updated_date = Column(
        Date, server_default=func.current_date(), onupdate=func.current_date()
    )
