from datetime import datetime
from fastapi import Depends
from sqlalchemy import func, insert, select, update
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
from pydantic import BaseModel
from src.api.schemas.currencies_schema import CurrencyResponseModel, AvailableCurrencies
from src.infrastructure.database.database import get_session
from src.infrastructure.database.models.currency import CurrencyDBModel
from enum import Enum


class AbstractCurrencyUseCase(ABC):
    @abstractmethod
    def get_last_updated_time(self):
        pass

    @abstractmethod
    def save_all(self):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass


AvailableCurrencies


class CurrencyDbRepository:
    def __init__(self, session: Session = Depends(get_session)):
        self.session: Session = session

    async def save_all(self, currencies: CurrencyResponseModel) -> dict[str, str]:
        query = select(func.count()).select_from(CurrencyDBModel)
        result = await self.session.execute(query)
        count = result.scalar()

        if count == 0:
            values = []
            currency_rates = currencies["rates"]
            for code, exchange_rate in currency_rates.items():
                values.append({
                    "name": AvailableCurrencies[code].value,
                    "code": code,
                    "exchange_rate": exchange_rate,
                })
            await self.session.execute(insert(CurrencyDBModel).values(values))
        else:
            currency_rates = currencies["rates"]
            for code, exchange_rate in currency_rates.items():
                query = update(CurrencyDBModel).where(
                    CurrencyDBModel.code == code).values(exchange_rate=exchange_rate, updated_at=func.now())
                await self.session.execute(query)

        await self.session.commit()
        return {"status": "ok"}

    async def get_last_updated_time(self):
        last_updated = await self.session.execute(
            func.max(CurrencyDBModel.updated_at))
        return last_updated.scalar()

    async def get_all(self):
        query = select(CurrencyDBModel).order_by(CurrencyDBModel.id)
        currencies = await self.session.execute(query)
        return currencies.scalars().all()

    async def currencies_convert(self, convert_from: AvailableCurrencies, convert_to: AvailableCurrencies):
        convert_from_in_db = await self.session.execute(
            select(CurrencyDBModel).
            where(CurrencyDBModel.code == convert_from.name)
        )
        convert_from_in_db = convert_from_in_db.scalar()

        convert_to_in_db = await self.session.execute(
            select(CurrencyDBModel).
            where(CurrencyDBModel.code == convert_to.name)
        )
        convert_to_in_db = convert_to_in_db.scalar()

       
        return convert_from_in_db, convert_to_in_db
