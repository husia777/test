from datetime import datetime
from fastapi import Depends
from src.api.schemas.currencies_schema import AvailableCurrencies

from src.repositories.currency.currency_db_repository import CurrencyDbRepository


class CurrencyService:
    def __init__(self, repository: CurrencyDbRepository = Depends()) -> None:
        self.repository: CurrencyDbRepository = repository

    async def save_all(self, currencies) -> dict[str, str]:
        return await self.repository.save_all(currencies)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_last_updated_time(self):
        last_updated = await self.repository.get_last_updated_time()
        last_updated = datetime.fromisoformat(str(last_updated))
        return last_updated.strftime("%Y-%m-%d %H:%M:%S")

    async def currencies_convert(self, convert_from: AvailableCurrencies,
                                 convert_to: AvailableCurrencies, quantity: int):

        convert_from_in_db, convert_to_in_db = await self.repository.currencies_convert(convert_from, convert_to)
        return f"{quantity} {convert_from_in_db.name} equals {(convert_to_in_db.exchange_rate / convert_from_in_db.exchange_rate) * quantity} {convert_to_in_db.name}"
