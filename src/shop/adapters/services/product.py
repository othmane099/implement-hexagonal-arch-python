from src.shop.domain.model import schema
from src.shop.domain.model.model import product_factory
from src.shop.domain.model.schema import ProductDTO
from src.shop.domain.ports.services.product import ProductService
from src.shop.domain.ports.unit_of_work.product import ProductUnitOfWork


class ProductServiceImpl(ProductService):
    def __init__(self, uow: ProductUnitOfWork):
        self.uow = uow

    def create_product(self, dto: schema.ProductDTO):
        with self.uow:
            schema_ = ProductDTO.model_dump(dto)
            model_ = product_factory(**schema_)
            self.uow.repository.add(model_)
            self.uow.commit()
