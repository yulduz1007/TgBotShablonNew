import datetime

from sqlalchemy import String, BigInteger, DateTime, Column, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase, declared_attr

from db.utils import AbstractClass


class Base(AsyncAttrs, DeclarativeBase):
    @declared_attr
    def __tablename__(self):
        return self.__name__.lower() + "s"

class CreatedModel(Base, AbstractClass):
    __abstract__ = True

    created_at = Column(DateTime(), default=datetime.datetime.utcnow, server_default=func.now())
    updated_at = Column(DateTime() , onupdate=datetime.datetime.utcnow,default=datetime.datetime.utcnow,server_default=func.now())

class User(CreatedModel):
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    fullname: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(255), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)