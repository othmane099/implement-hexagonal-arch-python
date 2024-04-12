def test_uow_add_product(get_fake_product_uow, get_product_model_object):
    with get_fake_product_uow:
        get_fake_product_uow.repository.add(get_product_model_object)
        all_ = get_fake_product_uow.repository.get_all()
        values = list(all_.values())
        assert len(values) == 1
        assert values[0] == get_product_model_object
