from typing import Optional
from datetime import datetime

from sqlalchemy_utils import EmailType
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    email: str

    class Config:
        orm_mode = True