"""
Работа с бд
"""
from app.api.db import table, database


async def get_item(id):
    query = table.select(table.c.id == id)
    return await database.fetch_one(query=query)


async def get_all_items():
    query = table.select()
    return await database.fetch_all(query=query)
