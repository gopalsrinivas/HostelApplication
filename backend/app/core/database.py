from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from app.core.config import settings
from app.core.logging import logging


async_engine = create_async_engine(settings.DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

def get_session() -> AsyncSession:
    return async_session()
