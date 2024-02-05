from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User

from schemas.user import UserCreate


async def create_user(
    new_user: UserCreate,
    session: AsyncSession,
) -> User:
    new_user_data = new_user.dict()
    db_user = User(**new_user_data)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def get_user_by_name(
    user_name: str,
    session: AsyncSession,
) -> None:
    user = await session.execute(
        select(
            User
        ).where(
            User.name == user_name
        )
    )
    return user.scalars().first()