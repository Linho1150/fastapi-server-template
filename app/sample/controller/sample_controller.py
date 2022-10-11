from typing import Optional
from functools import lru_cache

from fastapi import APIRouter, Request, Depends
from pydantic import BaseModel
from core.config import config

router = APIRouter(
    prefix="/samples",
    tags=["samples"],
    responses={404: {"description": "Not found"}}, )


@lru_cache()
def getConfig():
    # lru_cache is read env file only once
    return config.Settings()


class Item(BaseModel):
    name: str
    description: str
    age: int
    sex: Optional[str] = None


@router.post("/", response_model=Item, tags=["samples"], summary='this is sample api')
async def sample(item: Item, request: Request) -> Item:
    # todo: make get api for sample

    """ This is Just Sample Code for post api with Google docstring
    Args:
        item: Request name, description, age, sex
        request (): Get body type
    Returns:
        return input name & description & age & sex
    """
    result: Item = await request.json()
    return result


@router.get("/")
async def get_config_setting(settings: config.Settings = Depends(getConfig)):
    return {
        "app_name": settings.app_name,
        "items_per_user": settings.items_per_user,
        "admin_email": settings.admin_email,
    }
