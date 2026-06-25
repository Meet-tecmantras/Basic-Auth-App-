from app.models.user import UserCreate, UserLogin


class AuthService:
    def register(self, payload: UserCreate):
        return {"email": payload.email, "message": "User registered successfully"}

    def login(self, payload: UserLogin):
        return {"access_token": "demo-token", "token_type": "bearer"}


auth_service = AuthService()
