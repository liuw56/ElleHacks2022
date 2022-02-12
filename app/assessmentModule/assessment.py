from fastapi import APIRouter

router = APIRouter(
    prefix="/assess",
    tags=["assessment"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_assessment() -> str:
    return {"This is the assessment api"}
