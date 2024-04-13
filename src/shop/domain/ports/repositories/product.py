from abc import ABC, abstractmethod

from src.shop.domain.model import model
from src.shop.domain.model.model import Product


class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: model.Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id_: int):
        raise NotImplementedError

    @abstractmethod
    def get(self, id_) -> model.Product:
        raise NotImplementedError

    @abstractmethod
    def get_by_name(self, name: str) -> model.Product:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[model.Product]:
        raise NotImplementedError
