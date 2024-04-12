from sqlalchemy import (
    BigInteger,
    Column,
    Integer,
    MetaData,
    String,
    Table,
    Float,
)
from sqlalchemy.orm import registry

from src.shop.domain.model.model import Product

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

product = Table(
    "products",
    mapper_registry.metadata,
    # Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column(
        "id",
        BigInteger().with_variant(Integer, "sqlite"),
        primary_key=True,
        autoincrement=True,
    ),
    Column("name", String, nullable=False),
    Column("price", Float, nullable=False),
    Column("stock", Integer, nullable=False),
)


def start_mappers():
    mapper_registry.map_imperatively(Product, product)
