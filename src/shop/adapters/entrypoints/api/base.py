from fastapi import APIRouter

from .v1 import route_product

api_router = APIRouter()

api_router.include_router(
    route_product.router, prefix="/product", tags=["product"]
)
