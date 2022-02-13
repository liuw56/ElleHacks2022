from fastapi import APIRouter
from data import Data
router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_farms():
    return Data.FARMS


@router.get("/{farmId}")
async def get_farm(farmId):
    farm = Data.FARMS.get(farmId)
    return farm


@router.get("/{farmId}/items")
async def get_items(farmId):
    return Data.ITEM
