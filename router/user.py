from fastapi.responses import JSONResponse
from utils.jwt_manager import create_token
from fastapi import APIRouter
from schemas.user import User

auth_router = APIRouter()

@auth_router.post("/login", tags=['Auth'])
def login(user: User):
    if user.username == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.dict(), "secret_str")
    return JSONResponse(content={
        "message": "Login success",
        "token": token
    })