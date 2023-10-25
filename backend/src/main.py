from fastapi import FastAPI
from src.api.routes.currency import router as currency_router

app = FastAPI()
app.include_router(router=currency_router)