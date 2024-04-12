from typing import List

from pydantic import BaseModel, EmailStr


class ProductDTO(BaseModel):
    name: str
    price: float
    stock: int
