from abc import ABC, abstractmethod

from src.shop.domain.ports.repositories.product import ProductRepository


class ProductUnitOfWork(ABC):
    repository: ProductRepository

    def __enter__(self) -> "ProductUnitOfWork":
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None:
            self.rollback()

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError
