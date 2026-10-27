from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base() 

# endpoint de conexão
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5437/track_money_db"

# Cria acesso para conectar ao banco de dados 

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Para excutar e comitar no banco de dados
def init_database():
    with engine.connect() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS authentication"))
        conn.commit()

# Para criar a tabela.
def crate_tables():
    Base.metadata.create_all(bind=engine)