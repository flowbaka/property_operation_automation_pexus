from sqlalchemy import URL, create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import settings


# Construct the PostgreSQL connection address
database_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.DB_USER,
    password=settings.DB_PASSWORD.get_secret_value(),
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    database=settings.DB_NAME,
)


# Manage PostgreSQL connections
engine = create_engine(
    database_url,
    pool_pre_ping=True,
)


# Parent class for all database models
class Base(DeclarativeBase):
    pass


# Creates database sessions for reading and saving data
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful:", result.scalar_one())


if __name__ == "__main__":
    test_connection()