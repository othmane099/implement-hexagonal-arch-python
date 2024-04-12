import pytest

from src.shop.adapters.repositories.fake_product_repository import FakeProductRepository
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
