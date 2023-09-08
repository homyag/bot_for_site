import logging
import datetime
from typing import List

from sqlalchemy import BigInteger, VARCHAR, Float, ForeignKey, DATE
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship

logger = logging.getLogger(__name__)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True, nullable=False
    )  # <- Идентификатор телеграм пользователя

    username: Mapped[str] = mapped_column(VARCHAR(32), unique=False,
                                          nullable=True)
    # дата регистрации
    reg_date: Mapped = mapped_column(DATE, default=datetime.date.today())
    # последнее обновление пользователя
    upd_date: Mapped = mapped_column(DATE, onupdate=datetime.date.today())

    fullname: Mapped[str] = mapped_column(VARCHAR(129), nullable=True)
    e_mail: Mapped[str] = mapped_column(VARCHAR(129), nullable=True)
    phone: Mapped[str] = mapped_column(VARCHAR(12), nullable=True)
    locale: Mapped[str] = mapped_column(VARCHAR(2), default="ru")

    products: Mapped[List['Product']] = relationship(
        back_populates="users", cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return f"<User:{self.id}>"


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    name: Mapped[str] = mapped_column(VARCHAR(32), nullable=False)
    article: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    model: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)

    user: Mapped["User"] = relationship(back_populates="products")

    @property
    def products_to_dict(self) -> dict:
        return {i.name: getattr(self, i.name) for i in
                self.__tablename__.columns}
