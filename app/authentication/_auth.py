import os
from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from app.authentication._user import User


def generate_jwt_token(user: User) -> str:
    """Generate a JWT token for the user."""
    if not os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"): # Variavel de ambiente 
        raise ValueError("ACCESS_TOKEN_EXPIRE_MINUTES environment variable is not set.")

    expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)

    if not os.getenv("SECRET_KEY"): # Validando a secret_key
        raise ValueError("SECRET_KEY environment variable is not set.")
    if not os.getenv("ALGORITHM"):
        raise ValueError("ALGORITHM environment variable is not set.")

    # Preparando os atributos, para usar no jwt
    payload = {"sub": user.email, "name": user.name, "exp": expire}
    token = jwt.encode(
        payload, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM")
    )
    return token

# Faz o decote do JWT, para recuperar o token no tempo da requisição
def get_email_from_token(
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="users/token")),
) -> str:
    #testa se o token está correto
    try:
        payload = jwt.decode(
            token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")]
        )
        email: str = payload.get("sub")
        # Se não localizar o e-mail acoplado ao token
        if not email:
            raise HTTPException(
                status_code=401, detail="Could not validate credentials"
            )
        return email
    except Exception:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
