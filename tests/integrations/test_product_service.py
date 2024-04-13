from src.shop.config.containers import Container
from src.shop.domain.model.schema import ProductDTO


def test_product_service_add(get_fake_container, get_product_service_impl):
    with Container.product_uow.override(get_fake_container.product_uow):
        get_product_service_impl.create_product(ProductDTO(name="lkj", price=100, stock=1))
        uow_ = get_fake_container.product_uow()
        with uow_:
            result = uow_.repository.get_all()
            assert len(result) == 1