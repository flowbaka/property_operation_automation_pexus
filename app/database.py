from sqlalchemy import URL, create_engine, text

from app.config import settings


# Safely construct the PostgreSQL connection address
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD.get_secret_value(),
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


# Create the database connection manager
engine = create_engine(
    database_url,
    pool_pre_ping=True,
)


def test_connection():
    """Check whether Python can communicate with PostgreSQL."""

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful:", result.scalar_one())


if __name__ == "__main__":
    test_connection()