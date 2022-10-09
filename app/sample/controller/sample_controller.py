from typing import Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(
    prefix="/samples",
    tags=["samples"],
    responses={404: {"description": "Not found"}}, )


class Item(BaseModel):
    name: str
    description: str
    age: int
    sex: Optional[str] = None


@router.post("/", response_model=Item, tags=["samples"], summary=["this is sample api"])
async def sample(item: Item, request: Request) -> Item:
    # todo: make get api for sample

    """ This is Just Sample Code for post api with Google docstring
    Args:
        item: Request name, description, age, sex

    Returns:
        return input name & description & age & sex
    """
    result: Item = await request.json()
    return result
