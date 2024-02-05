from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from schemas.user import UserCreate
from crud.user import create_user
from .valid import check_name_duplicate

router = APIRouter()

@router.post(
    '/',
    response_model=UserCreate,
)
async def user_post(
    user: UserCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_name_duplicate(user.name, session)
    return await create_user(user, session)
