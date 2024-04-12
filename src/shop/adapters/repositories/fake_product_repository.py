import random

from src.shop.domain.model import model
from src.shop.domain.ports.repositories.product import ProductRepository


class FakeProductRepository(ProductRepository):
    def __init__(self):
        super().__init__()
        self.database = {}

    def add(self, product: model.Product) -> None:
        id_ = random.randint(10, 100)
        self.database[id_] = product

    def delete_by_id(self, id: int):
        del self.database[id]

    def get(self, id_) -> model.Product:
        return self.database[id_]

    def get_by_name(self, name: str) -> model.Product:
        for val in self.database.values():
            if val.name == name:
                return val

    def get_all(self) -> dict[int, model.Product]:
        return self.database
