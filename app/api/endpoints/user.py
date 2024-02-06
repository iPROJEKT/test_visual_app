from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.schemas.user import UserBase, UserGet
from app.crud.user import create_user, get_all_user, get_user_by_id, remove
from .valid import check_name_duplicate, check_email_duplicate

router = APIRouter()

@router.post(
    '/',
    response_model=UserBase,
)
async def user_post(
    user: UserBase,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(user.user_name, session)
    await check_email_duplicate(user.email, session)
    return await create_user(user, session)


@router.get(
    '/',
)
async def user_post(
    session: AsyncSession = Depends(get_async_session),
):
    return await get_all_user(session)


@router.get(
    '/{user_id}',
)
async def id_user_get(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    user = await (
        get_user_by_id(
            id=user_id, session=session
        )
    )
    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такого юзера нет'
        )

    return user


@router.delete(
    '/{user_id}',
)
async def id_user_dell(
    user_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    user = await (
        get_user_by_id(
            id=user_id, session=session
        )
    )
    if user is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такого юзера нет'
        )
    
    return await remove(await get_user_by_id(user_id, session), session)