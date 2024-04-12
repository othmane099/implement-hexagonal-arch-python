import pytest


@pytest.fixture(scope='module')
def get_fake_product_dict():
    return {
        "name": "Fake Product",
        "price": 10.99,
        "stock": 100
    }
