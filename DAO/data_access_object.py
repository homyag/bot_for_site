import logging
from typing import NoReturn, Any, Union, Optional
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.engine import ScalarResult
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.exc import (
    NoResultFound,
)

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
        #return [item.to_dict for item in result.scalars().all()]

    #  Merge object
    async def add_object(
        self,
        db_object: Union[User],
    ) -> None:
        await self.session.merge(db_object)

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