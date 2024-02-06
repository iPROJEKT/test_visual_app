from datetime import datetime

from sqlalchemy import Column, String, DateTime
from sqlalchemy_utils import EmailType

from app.core.db import Base


class User(Base):
    user_name = Column(
        String(100,),
        unique=True,
        nullable=False
    )
    email = Column(
        EmailType,
        unique=True
    )
    create_date = Column(
        DateTime,
        default=datetime.now
    )

