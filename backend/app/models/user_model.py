from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum
from datetime import datetime

class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"
    transgender = "Transgender"

class User(SQLModel, table=True):
    __tablename__ = 'user_details'
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    mobile: str
    gender: GenderEnum
    is_active: bool = Field(default=False)
    created_on: datetime = Field(default_factory=datetime.utcnow)
    updated_on: Optional[datetime] = Field(default=None, sa_column_kwargs={"onupdate": datetime.utcnow})
