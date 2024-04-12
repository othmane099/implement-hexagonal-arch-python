from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.shop.adapters.unit_of_work.product import ProductUnitOfWorkImpl
from src.shop.config.settings import get_database_uri

# Hard code the db connection for now
db_uri = get_database_uri()
ENGINE = create_engine(db_uri)


class FakeContainer(containers.DeclarativeContainer):
    DEFAULT_SESSION_FACTORY = lambda: sessionmaker(bind=ENGINE, autocommit=False)

    product_uow = providers.Factory(
        ProductUnitOfWorkImpl, session_factory=DEFAULT_SESSION_FACTORY
    )
