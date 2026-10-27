from fastapi import Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session


class UserCreate(BaseModel):
    email: str
    name: str
    password: str

def post_user(body: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    user = User(name=body.name, email=body.email, password=body.password)
    db.add(user)