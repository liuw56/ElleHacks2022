from fastapi import APIRouter
from data import Data
import json
router = APIRouter(
    prefix="/users",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{userId}")
async def get_user(userId: int) -> json:
    user = Data.USER_DATA.get(userId)
    return user
