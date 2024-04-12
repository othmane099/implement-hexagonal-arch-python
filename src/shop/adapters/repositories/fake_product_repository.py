import random

from src.shop.domain.model import model
from src.shop.domain.ports.repositories.product import ProductRepository


class FakeProductRepository(ProductRepository):
    def __init__(self):
        super().__init__()
        self.database = {}

    def _add(self, product: model.Product) -> None:
        id_ = random.randint(10, 100)
        self.database[id_] = product

    def _get(self, id_) -> model.Product:
        return self.database[id_]

    def _get_by_name(self, name: str) -> model.Product:
        for val in self.database.values():
            if val.name == name:
                return val

    def _get_by_uuid(self, uuid: str) -> model.Product:
        for val in self.database.values():
            if val.uuid == uuid:
                return val

    def _get_all(self) -> list[model.Product]:
        return list(self.database.values())
