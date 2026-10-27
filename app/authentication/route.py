from fastapi import APIRouter
from app.authentication.post_user import post_user

user_router = APIRouter()

user_router.add_api_route(
    path="/users",
    endpoint=post_user,
    methods=["POST"],
    response_model=None,
    status_code=201,
    tags=["users"],
    summary="Create a new user",
)

