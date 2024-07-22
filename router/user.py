from fastapi.responses import JSONResponse
from pydantic import BaseModel
from jwt_manager import create_token
from fastapi import APIRouter

auth_router = APIRouter()

# user model
class User(BaseModel):
    username: str
    password: str
    

@auth_router.post("/login", tags=['Auth'])
def login(user: User):
    if user.username == "admin@gmail.com" and user.password == "admin":
        token = create_token(user.dict(), "secret_str")
    return JSONResponse(content={
        "message": "Login success",
        "token": token
    })