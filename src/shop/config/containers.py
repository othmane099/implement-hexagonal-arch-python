from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.shop.adapters.services.product import ProductServiceImpl
from src.shop.adapters.unit_of_work.product import ProductUnitOfWorkImpl
from src.shop.config.settings import get_database_uri

db_uri = get_database_uri()
ENGINE = create_engine(db_uri)


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        modules=[
            "src.shop.adapters.services.product",
        ],

        packages=[
            "src.shop.adapters.entrypoints.api",
        ],
    )

    DEFAULT_SESSION_FACTORY = lambda: sessionmaker(bind=ENGINE, autocommit=False)

    product_uow = providers.Factory(
        ProductUnitOfWorkImpl, session_factory=DEFAULT_SESSION_FACTORY
    )

    product_service = providers.Factory(
        ProductServiceImpl,
        uow=product_uow,
    )
