from sqlalchemy import Column, Integer, String

class User:
    # CRIANDO A TABELA, SEPARANDO POS schema PARA MANTER UM MONOLITO MODULAR
    __tablename__ = 'users'
    __table_args__ = {'schema': "authentication"}

    # MAPEANDO O BANCO DE DADOS
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128))
    email = Column(String(128), unique=True, index=True)
    hashed_password = Column(String(512))

    