from src.models import Base, dto_factory
from sqlalchemy import Column, Float, Integer, String

__all__ = ["User", "CreateUserDTO"]

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    permissions = Column(Integer, default=0)

    def __repr__(self) -> dict:
        return {
            "id": self.id,
            "nickname": self.nickname,
            "email": self.email,
            "permissions": self.permissions,
        }


CreateUserDTO = dto_factory("CreateUserDTO", User, exclude=["id"])