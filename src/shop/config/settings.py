class Settings:
    # Imagine this is a true production database connection
    db_uri = (
        "sqlite:///tutorial.db"
    )


def get_database_uri() -> str:
    return Settings.db_uri
