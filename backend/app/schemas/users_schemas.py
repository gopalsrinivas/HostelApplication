from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: str
    mobile: str
    gender: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    mobile: str
    gender: str
    is_active: bool
    created_on: datetime
    updated_on: Optional[datetime]
    
    class Config:
        from_attributes = True
