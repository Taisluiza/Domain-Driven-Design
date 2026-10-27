from pydantic import BaseModel
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.infra import get_db
from app.authentication import User as _User

class UserCreate(BaseModel):
    email: str
    name: str
    password: str

def post_user(body: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    user = _User(name=body.name, email=body.email, password=body.password)
    db.add(user)
    db.commit()
    db.refresh(user)


    return JSONResponse(
        status_code=201,
        content=None,
        headers={"Location": f"/users/{user.id}"},
    )