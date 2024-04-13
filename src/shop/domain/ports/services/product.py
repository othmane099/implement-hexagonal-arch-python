from abc import ABC, abstractmethod

from src.shop.domain.model import model, schema
from src.shop.domain.ports.unit_of_work.product import ProductUnitOfWork


class ProductService(ABC):

    @abstractmethod
    def __init__(self, uow: ProductUnitOfWork):
        raise NotImplementedError

    @abstractmethod
    def create_product(self, product: schema.ProductDTO) -> schema.ProductDTO:
        raise NotImplementedError


    @abstractmethod
    def all_products(self):
        raise NotImplementedError

