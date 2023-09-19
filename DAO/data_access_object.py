import logging
from typing import NoReturn, Union, Optional

from sqlalchemy import select
from sqlalchemy.sql.functions import max, func
from sqlalchemy.engine import ScalarResult
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import aliased

from database.models import User, Product, Order

logger = logging.getLogger(__name__)


class DataAccessObject:
    def __init__(self, session: AsyncSession) -> NoReturn:
        self.session: AsyncSession = session

    #  Get object from id
    async def get_object(
            self, db_object: Union[User], db_object_id: int = None
    ) -> Optional[User]:
        stmt = select(db_object)
        if db_object_id:
            stmt = stmt.where(db_object.id == db_object_id)

        result: ScalarResult = await self.session.execute(stmt)
        return result.scalars().first()
        # return [item.to_dict for item in result.scalars().all()]

    #  Merge object
    async def add_object(
            self,
            db_object: Union[User],
    ) -> None:
        await self.session.merge(db_object)

    # users who check price
    async def get_users_with_contacts(self):
        stmt = select(User).filter(User.e_mail.isnot(None),
                                   User.phone.isnot(None))
        result: ScalarResult = await self.session.execute(stmt)
        return result.scalars().all()

    # get all users
    async def get_all_users(self):
        stmt = select(User)
        result: ScalarResult = await self.session.execute(stmt)
        return result.scalars().all()

    #  Order
    async def get_order(
            self, db_object: Union[Order], db_object_id: int = None
    ) -> Optional[Order]:
        stmt = select(db_object)
        if db_object_id:
            stmt = stmt.where(db_object.id == db_object_id)
            result: ScalarResult = await self.session.execute(stmt)
            return result.scalars().first()

    async def add_order(
            self,
            db_object: Union[Order],
    ) -> None:
        await self.session.merge(db_object)

    # получение списка всех заказов
    async def get_all_orders(self) -> list[Order]:
        stmt = select(Order)
        result: ScalarResult = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_all_orders_with_user_data(self) -> list[dict]:
        users_alias = aliased(User)
        orders_alias = aliased(Order)

        query = (
            select(
                users_alias.username,
                users_alias.fullname,
                users_alias.phone,
                orders_alias.name,
                orders_alias.price,
                orders_alias.description,
                orders_alias.order_date
            )
            .join(orders_alias, users_alias.id == orders_alias.user_id)
            .group_by(users_alias.username, users_alias.fullname,
                      users_alias.phone, orders_alias.name, orders_alias.price,
                      orders_alias.description, orders_alias.order_date)
        )

        result = await self.session.execute(query)
        rows = result.all()

        # Создайте список словарей вручную, указав ключи и значения
        orders_with_user_data = [
            {
                "username": row[0],
                "fullname": row[1],
                "phone": row[2],
                "name": row[3],
                "price": row[4],
                "description": row[5],
                "order_date": row[6]
            }
            for row in rows
        ]

        return orders_with_user_data

    # Product
    async def get_product(
            self, db_object: Union[Product], db_object_id: int = None
    ) -> Optional[Product]:
        stmt = select(db_object)
        if db_object_id:
            stmt = stmt.where(db_object.id == db_object_id)
            result: ScalarResult = await self.session.execute(stmt)
            return result.scalars().first()

    async def add_product(
            self,
            db_object: Union[Product],
    ) -> None:
        await self.session.merge(db_object)

    async def get_user_orders(self, user_id: int) -> list[dict]:
        users_alias = aliased(User)
        orders_alias = aliased(Order)

        query = (
            select(
                orders_alias.name,
                orders_alias.price
            )
            .join(users_alias, users_alias.id == orders_alias.user_id)
            .where(users_alias.id == user_id)
            # Фильтр по Telegram ID пользователя
        )

        result = await self.session.execute(query)
        rows = result.all()

        # Создайте список словарей с заказами пользователя
        user_orders = [
            {
                "name": row[0],
                "price": row[1],
            }
            for row in rows
        ]

        return user_orders
