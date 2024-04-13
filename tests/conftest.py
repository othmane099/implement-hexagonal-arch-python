import contextlib

import pytest
import pytest_asyncio
import sqlalchemy
from httpx import AsyncClient

from src.shop.adapters.db.orm import start_mappers
from src.shop.adapters.entrypoints.api.app import app
from src.shop.adapters.repositories.fake_product_repository import FakeProductRepository
from src.shop.adapters.services.product import ProductServiceImpl
from src.shop.adapters.unit_of_work.fake_product_uow import FakeProductUnitOfWork
from src.shop.config.fake_container import FakeContainer
from src.shop.domain.model.model import product_factory


@pytest.fixture(scope='module')
def get_fake_product_dict():
    return {
        "name": "Fake Product",
        "price": 10.99,
        "stock": 100
    }


@pytest.fixture(scope="module")
def get_product_model_object():
    return product_factory(**{
        "name": "Fake Product",
        "price": 10.99,
        "stock": 100
    })


@pytest.fixture(scope="module")
def get_fake_product_repository():
    return FakeProductRepository()


@pytest.fixture(scope="module")
def get_fake_product_uow():
    return FakeProductUnitOfWork()


@pytest.fixture(scope="module")
def get_fake_container():
    # Start ORM mapper
    with contextlib.suppress(sqlalchemy.exc.ArgumentError):
        start_mappers()

    # Truncate table
    uow = FakeContainer.product_uow()
    with uow:
        uow.session.execute(
            sqlalchemy.text("DELETE FROM products")
        )
        uow.commit()

    return FakeContainer()


@pytest.fixture(scope="module")
def get_product_service_impl():
    return ProductServiceImpl()


@pytest_asyncio.fixture()
async def client():
    async with AsyncClient(
        app=app, base_url="http://127.0.0.1:8001/product/"
    ) as client:
        yield client
