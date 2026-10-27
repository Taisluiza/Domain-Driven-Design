from fastapi import Depends
from sqlalchemy.orm import Session

from app.authentication._user import _User
from app.infra.database import get_db


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: _User):
        """
        Create a new user in the database.
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

    def get_by_email(self, email: str) -> _User | None:
        """
        Retrieve a user by email.
        """
        return self.db.query(_User).filter(_User.email == email).first()


def get_user_repository(db: Session = Depends(get_db)) -> UserRepository:
    """
    Dependency to get a UserRepository instance.
    """
    return UserRepository(db)
