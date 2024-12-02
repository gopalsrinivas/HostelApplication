from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class Hostel(SQLModel, table=True):
    __tablename__ = "hostel_details"

    id: int = Field(default=None, primary_key=True, autoincrement=True)
    hostel_id: str = Field(sa_column=Field(nullable=False, unique=True))
    name: Optional[str] = Field(default=None, nullable=True)
    is_active: bool = Field(default=False)
    created_on: datetime = Field(default=datetime.utcnow, nullable=False)
    updated_on: Optional[datetime] = Field(default=None, nullable=True)
