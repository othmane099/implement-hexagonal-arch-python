from typing import Callable, Any

from sqlalchemy.orm import Session

from src.shop.adapters.repositories.product import ProductRepositoryImpl
from src.shop.domain.ports.unit_of_work.product import ProductUnitOfWork


class ProductUnitOfWorkImpl(ProductUnitOfWork):
    def __init__(self, session_factory: Callable[[], Any]):
        self.session_factory = session_factory()

    def __enter__(self):
        self.session: Session = self.session_factory()
        self.repository = ProductRepositoryImpl(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
