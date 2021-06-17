"""
Вроде как вьюхи
"""
from typing import List

from fastapi import APIRouter, HTTPException

from app.api.models import OneItem
from app.api import db_manager

movies = APIRouter()


@movies.get('/', response_model=List[OneItem])
async def all_items():
    return await db_manager.get_all_items()


@movies.get('/{id}/')
async def one_item(id: int):
    movie = await db_manager.get_item(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie
