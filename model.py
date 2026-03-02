from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import date as dt
from sqlalchemy import Date, Integer, String


class Base(DeclarativeBase):
    pass


class People(Base):
    __tablename__ = "People"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[dt] = mapped_column(Date)
    age: Mapped[int] = mapped_column(Integer)
    country: Mapped[str] = mapped_column(String)
    gender: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    first_name: Mapped[str] = mapped_column(String)
