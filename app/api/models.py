"""
Модельки для обращениея к бд
"""
import datetime
from pydantic import BaseModel


class OneItem(BaseModel):
    """
    Для вывода одного элемента
    """
    id: int
    address: str
    datetime: datetime.datetime
