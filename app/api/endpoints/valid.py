from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud.user import get_user_by_name, get_user_by_email


async def check_name_duplicate(
    user_name: str,
    session: AsyncSession
) -> None:
    user = await (
        get_user_by_name(
            user_name=user_name, session=session
        )
    )
    if user is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такой пользователь уже сущетсвует'
        )


async def check_email_duplicate(
    email_name: str,
    session: AsyncSession
) -> None:
    user = await (
        get_user_by_email(
            email_name=email_name, session=session
        )
    )
    if user is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такой email уже сущетсвует'
        )
