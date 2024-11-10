from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from typing import Optional


class User(BaseModel):
    username: str
    email: EmailStr
    password: str
    hashed_password: Optional[str] = None

    def hash_password(self):
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.hashed_password = pwd_context.hash(self.password)
        self.password = None
        return self.hashed_password