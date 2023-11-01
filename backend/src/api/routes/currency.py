from fastapi import APIRouter, Depends
import requests
from src.config import API_FOR_SAVE_DATA, API_GET_SYMBOLS
from src.api.schemas.currencies_schema import AvailableCurrencies
from src.use_cases.currency_use_case import CurrencyService

router = APIRouter()


@router.get('/currencies/convert')
async def convert_currency(
    convert_from: AvailableCurrencies,
    convert_to: AvailableCurrencies,
    quantity: int | float,
    currency_service: CurrencyService = Depends(),
):
    return await currency_service.currencies_convert(convert_from, convert_to, quantity)


@router.get('/currencies')
async def get_all_currency(currency_service: CurrencyService = Depends()):
    return await currency_service.get_all()


@router.get("/currencies/save")
async def save_all_currencies(
    currency_service: CurrencyService = Depends(),
):
    data = requests.get(API_FOR_SAVE_DATA).json()
    symbols = requests.get(API_GET_SYMBOLS).json()
    return await currency_service.save_all(data, symbols)


@router.get("/currencies/info")
async def get_last_updated_time(currency_service: CurrencyService = Depends()) -> str:
    time_of_last_update = await currency_service.get_last_updated_time()
    return f"the time of the last update of the table is equal to {time_of_last_update}"
