from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4

app = FastAPI()

post = []

# post model
class Post(BaseModel):
    title: str
    content: Optional[str]
    create_at: datetime = datetime.now()
    

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/posts")
def read_posts():
    return post

@app.post("/posts")
def create_post(new_post: Post):
    new_post.id = str(uuid4())
    post.append(new_post)
    return post[-1]


@app.get("/posts/{post_id}")
def read_post(post_id: int):
    for p in post:
        if p["id"] == post_id:
            return p
    raise HTTPException(status_code=404, detail="Post not found")