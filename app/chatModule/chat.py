from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_users():
    return {"This is the chat api"}
