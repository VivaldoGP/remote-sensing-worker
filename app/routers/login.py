from fastapi import APIRouter
from app.schemas.user import User

router = APIRouter()


@router.post("/signup")
async def signup(user: User):
    user.hash_password()
    return {"message": f"{user}"}

@router.post("/login")
async def login(user: User):
    return {"message": f"Login with user: {user.username}"}

