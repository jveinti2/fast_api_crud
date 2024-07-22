from fastapi import FastAPI
from config.database import engine, Base  
from middlewares.error_handler import ErrorHandler
from router.post import post_router


app = FastAPI()
app.title = "FastAPI CRUD test"
app.description = "This is a very simple CRUD test with FastAPI"
app.version = "0.1"

app.add_middleware(ErrorHandler)
app.include_router(post_router)

Base.metadata.create_all(bind=engine)