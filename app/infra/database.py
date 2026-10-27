import os

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base() 

# endpoint de conexão

# Cria acesso para conectar ao banco de dados 
_engine: Engine | None = None
_session_local: sessionmaker | None = None


# Aqui vai trabalhar com a variavel global
def get_engine() -> Engine:
    global _engine
    if _engine is None:
        if not os.getenv("DATABASE_URL"):
            raise ValueError("DATABASE_URL environment variable is not set.")

        _engine = create_engine(os.getenv("DATABASE_URL"))
    return _engine


def get_session_local() -> sessionmaker:
    global _session_local
    if _session_local is None:
        _session_local = sessionmaker(
            autocommit=False, autoflush=False, bind=get_engine()
        )
    return _session_local


def get_db():
    SessionLocal = get_session_local()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_database():
    engine = get_engine()
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS authentication"))
        conn.commit()


def create_tables():
    engine = get_engine()
    from app.authentication._user import (
        _User,  # noqa: F401 - Import required for SQLAlchemy model discovery
    )

    Base.metadata.create_all(bind=engine)