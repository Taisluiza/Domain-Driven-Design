from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ELE VALIDA SE A SENHA ESTÁ CERTA JUNTAMENTE COM A CRIPTOGRAFIA, ELE GERA UM HASHED PARA VALIDAR SE ´´E IGUAL AO DO BANCO DE DADOS.

def get_password_hash(password: str) -> str:
    """Generate a hashed password using bcrypt."""
    return pwd_context.hash(password)

