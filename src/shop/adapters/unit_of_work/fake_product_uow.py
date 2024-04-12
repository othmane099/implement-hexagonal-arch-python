from src.shop.adapters.repositories.fake_product_repository import FakeProductRepository
from src.shop.domain.ports.unit_of_work.product import ProductUnitOfWork


class FakeProductUnitOfWork(ProductUnitOfWork):
    def __init__(self):
        self.committed = False

    def __enter__(self):
        self.repository = FakeProductRepository()
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)

    def commit(self):
        self.committed = True

    def rollback(self):
        # because we don't care
        pass
