from fastapi import FastAPI

from app.routers import auth

app = FastAPI(title="Basic Auth App")
app.include_router(auth.router, prefix="/auth", tags=["auth"])


@app.get("/")
def root():
    return {"message": "Basic Auth App API is running"}
