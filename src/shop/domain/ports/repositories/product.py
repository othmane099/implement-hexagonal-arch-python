from abc import ABC, abstractmethod

from src.shop.domain.model import model


class ProductRepository(ABC):
    @abstractmethod
    def _add(self, product: model.Product) -> None:
        raise NotImplementedError

    @abstractmethod
    def _get(self, id_) -> model.Product:
        raise NotImplementedError

    @abstractmethod
    def _get_by_name(self, name: str) -> model.Product:
        raise NotImplementedError

    @abstractmethod
    def _get_by_uuid(self, uuid: str) -> model.Product:
        raise NotImplementedError

    @abstractmethod
    def _get_all(self) -> list[model.Product]:
        raise NotImplementedError
