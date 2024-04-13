from dataclasses import dataclass, asdict
from typing import List, Any

from .schema import ProductDTO


@dataclass
class Product:
    name: str
    price: float
    stock: int

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def product_factory(**kwargs: dict[str, Any]) -> Product:
    ProductDTO.model_validate(kwargs)
    model_ = Product(**kwargs)
    return model_
