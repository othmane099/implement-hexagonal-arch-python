from dataclasses import dataclass
from typing import List, Any

from src.shop.domain.model.schema import ProductDTO


@dataclass
class Product:
    uuid: str
    name: str
    price: float
    stock: int


def product_factory(**kwargs: dict[str, Any]) -> Product:
    ProductDTO.model_validate(kwargs)
    model_ = Product(**kwargs)
    return model_
