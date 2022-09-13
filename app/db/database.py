from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:vmar26@localhost/test_project"

engine = create_engine(DATABASE_URL, echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)


def get_session() -> SessionLocal:  # session generator for Depends class
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
