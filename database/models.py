import logging
import datetime
from typing import List, Optional

from sqlalchemy import BigInteger, VARCHAR, Float, DATE, Integer, String, \
    ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.connect import Base

logger = logging.getLogger(__name__)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        BigInteger, primary_key=True, unique=True, nullable=False
    )  # <- Идентификатор телеграм пользователя

    username: Mapped[str] = mapped_column(VARCHAR(32), unique=False,
                                          nullable=True)
    # дата регистрации
    reg_date: Mapped[datetime.date] = mapped_column(DATE,
                                                    default=datetime.date.today())
    # последнее обновление пользователя
    upd_date: Mapped[datetime.date] = mapped_column(DATE,
                                                    onupdate=datetime.date.today(), nullable=True)

    fullname: Mapped[str] = mapped_column(VARCHAR(129), nullable=True)
    e_mail: Mapped[str] = mapped_column(VARCHAR(129), nullable=True)
    phone: Mapped[str] = mapped_column(VARCHAR(12), nullable=True)
    locale: Mapped[str] = mapped_column(VARCHAR(2), default="ru")

    products: Mapped[List['Product']] = relationship(
        'Product', back_populates="users", cascade="all, delete-orphan"
    )

    def __str__(self) -> str:
        return f"<User:{self.id} {self.username}>"

    @property
    def to_dict(self) -> dict:
        """
        Конвертирует модель в словарь
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Product(Base):
    __tablename__ = 'products'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'),
                                         nullable=False)
    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(129), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, nullable=False)
    subcategory_id: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(1000),
                                                       nullable=True)

    # Связь с пользователями
    users: Mapped[List['User']] = relationship(
        'User', back_populates='products'
    )

    def __repr__(self) -> str:
        return f"Product(product_id={self.product_id!r}, name={self.name!r}, price={self.price!r})"
