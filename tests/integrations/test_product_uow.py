def test_uow_add_product(get_fake_container, get_product_model_object):
    uow = get_fake_container.product_uow()
    with uow:
        uow.repository.add(get_product_model_object)
        uow.commit()
        all_ = uow.repository.get_all()
        assert len(all_) == 1


