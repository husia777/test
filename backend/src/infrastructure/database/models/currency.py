
from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.sql import func
from src.infrastructure.database.database import Base
from sqlalchemy.orm import Mapped, mapped_column 

class CurrencyDBModel(Base):
    __tablename__ = "currency"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    code: Mapped[str] = mapped_column(nullable=False)
    exchange_rate: Mapped[float] = mapped_column(nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now())