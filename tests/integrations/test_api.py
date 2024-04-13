import pytest

from src.shop.adapters.entrypoints.api.app import app

@pytest.mark.asyncio
async def test_get_all_calculation_api(get_fake_container, client):
    product_service = get_fake_container.product_service_impl()
    with app.container.product_service.override(product_service):
        response = await client.get("/products")
        assert response.status_code == 200

