from dataclasses import asdict

from dependency_injector.wiring import Provide

from src.shop.domain.model import schema
from src.shop.domain.model.model import product_factory, Product
from src.shop.domain.model.schema import ProductDTO
from src.shop.domain.ports.services.product import ProductService
from src.shop.domain.ports.unit_of_work.product import ProductUnitOfWork


class ProductServiceImpl(ProductService):
    def __init__(self, uow: ProductUnitOfWork = Provide["product_uow"]):
        self.uow = uow

    def create_product(self, dto: schema.ProductDTO) -> ProductDTO:
        with self.uow:
            schema_ = ProductDTO.model_dump(dto)
            model_ = product_factory(**schema_)
            product = self.uow.repository.add(model_)
            self.uow.commit()
            return ProductDTO(name=product.name, price=product.price, stock=product.stock)

    def all_products(self):
        with self.uow:
            data = self.uow.repository.get_all()
        a = []
        for d in data:
            a.append(ProductDTO.model_dump(ProductDTO(name=d.name, price=d.price, stock=d.stock)))
        return a
