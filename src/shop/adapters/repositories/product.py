from src.shop.domain.model import model
from src.shop.domain.ports.repositories.product import ProductRepository


class ProductRepositoryImpl(ProductRepository):
    def __init__(self, session):
        super().__init__()
        self.session = session

    def add(self, product: model.Product) -> None:
        self.session.add(product)

    def get(self, id_: int) -> model.Product:
        return self.session.query(model.Product).filter_by(id=id_).first()

    def delete_by_id(self, id_: int):
        return self.session.query(model.Product).delete(id=id_).first()

    def get_by_name(self, name: str) -> model.Product:
        return self.session.query(model.Product).filter_by(name=name).first()

    def get_all(self) -> list[model.Product]:
        return self.session.query(model.Product).all()
