from fastapi import APIRouter
from app.schemas.auth import UserCreate
from app.services.auth_service import AuthService
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
router = APIRouter()
service = AuthService()

@router.post("/register")
async def register(user: UserCreate):
    await service.register(user)
    return {"message": "created"}

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    return await service.login(form_data)