import pydantic
import pytest
from pydantic import ValidationError

from src.shop.domain.model.model import Product, product_factory
from src.shop.domain.model.schema import ProductDTO


def test_if_product_is_created(get_fake_product_dict):
    fake_product = get_fake_product_dict
    result = ProductDTO.model_validate(fake_product)
    model_ = Product(**fake_product)
    assert model_.name == result.name and model_.price == result.price and model_.stock == result.stock


def test_if_product_is_created_with_factory(get_fake_product_dict):
    fake_product = get_fake_product_dict
    result = ProductDTO.model_validate(fake_product)
    model_ = product_factory(**fake_product)
    assert model_.name == result.name and model_.price == result.price and model_.stock == result.stock


def test_if_product_is_created_with_factory_and_with_wrong_types():
    fake_product_with_wrong_type = {
        "name": "Product Name",
        "price": "price",
        "stock": 100
    }
    with pytest.raises(ValidationError):
        product_factory(**fake_product_with_wrong_type)


def test_if_product_dto_created(get_fake_product_dict):
    fake_product = get_fake_product_dict
    schema_ = ProductDTO.model_validate(fake_product)
    assert fake_product == ProductDTO.model_dump(schema_)


def test_if_product_dto_can_be_created_with_wrong_types():
    fake_product = {
        "name": 1,
        "price": 10.99,
        "stock": 100
    }
    with pytest.raises(pydantic.ValidationError):
        ProductDTO.model_validate(fake_product)


def test_if_product_dto_can_be_created_with_extra_fields():
    result = ProductDTO.model_validate({"name": "Fake Product", "price": 5.0, "stock": 55, "sku": "fake_product"})
    # So the "fake" data should be excluded
    assert {"name": "Fake Product", "price": 5.0, "stock": 55} == ProductDTO.model_dump(result)


def test_if_product_dto_can_be_created_with_wrong_field_names():
    fake_product = {
        "product_name": "Fake Product",
        "price": 10.99,
        "stock": 100
    }
    with pytest.raises(pydantic.ValidationError):
        ProductDTO.model_validate(fake_product)


def test_if_operands_create_dto_can_be_created_with_missing_field_names():
    with pytest.raises(pydantic.ValidationError):
        ProductDTO.model_validate({
            "price": 10.99,
            "stock": 100
        })
