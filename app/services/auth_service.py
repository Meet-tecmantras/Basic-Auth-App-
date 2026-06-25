from app.models.user import UserCreate, UserLogin


class AuthService:
    def register(self, payload: UserCreate):
        return {"email": payload.email, "message": "User registered successfully"}

    def login(self, payload: UserLogin):
        return {"access_token": "demo-token", "token_type": "bearer"}

    def forget_password(self, email: str):
        return {"email": email, "message": "Password reset link sent"}

    def reset_password(self, token: str, new_password: str):
        return {"message": "Password reset successfully"}


auth_service = AuthService()
