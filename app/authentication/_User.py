from sqlalchemy import Column, Integer, String

from app.domain_exception import DomainException
from app.authentication._password import get_password_hash
from app.infra.database import Base

class _User(Base):
    # CRIANDO A TABELA, SEPARANDO POS schema PARA MANTER UM MONOLITO MODULAR
    __tablename__ = 'users'
    __table_args__ = {'schema': "authentication"}

    # MAPEANDO O BANCO DE DADOS
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), nullable=False)
    email = Column(String(128), unique=True, index=True, nullable=False)
    hashed_password = Column(String(512), nullable=False )

    def __init__(self, name: str, email: str, password: str):    
        
        DomainException.validate(
         name and len(name) <= 128, 
         "Name must be at most 128 characters long."
        )
        self.name = name

        DomainException.validate(
            email and len(email) <= 128,
            "Email must be a non-empty string with a maximum length of 128 characters.",
        )
        self.email = email

        DomainException.validate(
            password and len(password) >= 8,
            "Password must be a non-empty string with a minimum length of 8 characters.",
        )
        self.hashed_password = get_password_hash(password)
        