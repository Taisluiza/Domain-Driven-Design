from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.domain_exception import DomainException
from app.infra.database import Base
from app.subscription.plan._plan import Plan
from app.subscription.user._user import User


class UserPlan(Base):
    __tablename__ = "user_plans"
    __table_args__ = {"schema": "subscription"}
    id = Column(Integer, primary_key=True, index=True)
    # Relacionamento com o usuario
    user_id = Column(Integer, ForeignKey("subscription.users.id"), nullable=False)
    # Relacionamento com o banco
    plan_id = Column(Integer, ForeignKey(Plan.id), nullable=False)
    active = Column(Boolean, nullable=False, default=False)
    # Simular o cartão que vai usar, de uma forma basica e sem segurança
    credit_card = Column(String(24), nullable=True)
    created_at = Column(DateTime, nullable=False)

    user = relationship("app.subscription.user._user.User", back_populates="user_plans")
    plan = relationship(Plan)

    def __init__(
           self,
           plan: Plan,
           active: bool,
           credit_card: str | None,
       ):
           self.plan = plan
           self.active = active
           self.credit_card = credit_card
           self.created_at = datetime.now(timezone.utc)