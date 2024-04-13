import json
import os
import sys
from pathlib import Path

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Response, Depends

from src.shop.domain.model.schema import ProductDTO

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent.parent.parent.parent))
from src.shop.domain.ports.services.product import ProductService
from src.shop.config.containers import Container

sys.path.insert(0, os.getcwd())

router = APIRouter()


@router.get("/products", response_model=None)
@inject
def get_all_products(
        service: ProductService = Depends(Provide[Container.product_service]),
) -> Response:
    data = service.all_products()
    print("mlkjmlkj")
    print(data)
    return Response(
        content=json.dumps(data), media_type="application/json", status_code=200
    )


@router.post("/products", response_model=None)
@inject
def create_product(
        product_dto: ProductDTO,
        service: ProductService = Depends(Provide[Container.product_service]),
) -> Response:
    data = service.create_product(product_dto)
    return Response(
        content=ProductDTO.model_dump_json(data), media_type="application/json", status_code=200
    )
