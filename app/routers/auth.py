from fastapi import APIRouter, HTTPException, status

from app.models.user import UserCreate, UserLogin
from app.schemas.auth import Token, UserResponse
from app.services.auth_service import auth_service

router = APIRouter()


@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate):
    return auth_service.register(payload)


@router.post("/login", response_model=Token)
def login(payload: UserLogin):
    result = auth_service.login(payload)
    if not result:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return result
