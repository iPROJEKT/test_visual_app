import re

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    user_name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserGet(BaseModel):
    user_name: str
    id: int
    email: str
    create_date: datetime

    class Config:
        orm_mode = True
