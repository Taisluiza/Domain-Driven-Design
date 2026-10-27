from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.authentication._auth import generate_jwt_token
from app.authentication.user_repository import UserRepository, get_user_repository


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


async def create_token(
        # form_data é a forma que vai obter o usuario e user_repository conecta no banco de dados
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_repository: UserRepository = Depends(get_user_repository),
) -> TokenResponse:
    """Create a JWT token for the user."""
    user = user_repository.get_by_email(form_data.username)
    # Se não localiza o usuario
    if not user:
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid credentials"},
        )
    # Se a senha não estiver correta
    if not user.verify_password(form_data.password):
        return JSONResponse(
            status_code=401,
            content={"detail": "Invalid credentials"},
        )
    # Se der certo, gera o token
    token = generate_jwt_token(user)
    return TokenResponse(access_token=token)
