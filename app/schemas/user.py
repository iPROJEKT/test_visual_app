import re

from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: EmailStr

    class Config:
        orm_mode = True

