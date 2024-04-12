def test_add_product(get_fake_product_repository, get_product_model_object):
    get_fake_product_repository.add(get_product_model_object)
    all_ = get_fake_product_repository.get_all()
    values = list(all_.values())
    assert len(values) == 1
    assert values[0] == get_product_model_object


def test_get_product_by_name(get_fake_product_repository):
    product = get_fake_product_repository.get_by_name("Fake Product")
    assert product.name == "Fake Product"


def test_delete_product_by_id(get_fake_product_repository):
    all_ = get_fake_product_repository.get_all()
    ids = list(all_.keys())
    get_fake_product_repository.delete_by_id(ids[0])
    values = list(all_.values())
    assert len(values) == 0
