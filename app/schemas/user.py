import re

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserGet(UserBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True
