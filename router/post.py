from typing import List
from fastapi import Body, Depends, HTTPException, Path
from fastapi.responses import JSONResponse
from config.database import Session
from models.post import Post as PostModel
from middlewares.jwt_bearer import JWTBearer
from fastapi import APIRouter, Body, Depends, HTTPException
from services.post import PostServices
from schemas.post import Post

post_router = APIRouter()
  
@post_router.get("/")
def read_root():
    return {"Hello": "World"}



@post_router.get("/posts", tags=['Post'], response_model=List[Post])
def read_posts() ->List[Post]:
    db = Session()
    try:
        posts = PostServices(db).get_posts()
        return posts
    finally:
        db.close()


@post_router.get("/posts/{post_id}", response_model=Post)
def read_post(post_id: int = Path(ge=1, le=100)) -> PostModel:
    db = Session()
    try:
        result = PostServices(db).get_post(post_id)
        if not result:
            raise HTTPException(status_code=404, detail="Post not found")
        return result
    finally:
        db.close()


@post_router.put("/posts/{post_id}")
def update_post(post_id: int, new_post: Post):
    db = Session()
    try:
        post = read_post(post_id)
        for key, value in new_post.dict().items():
            setattr(post, key, value)
        db.commit()
        db.refresh(post)
        return JSONResponse(content={"message": "Post updated successfully"}, status_code=200)
    finally:
        db.close()


@post_router.post("/posts", dependencies=[Depends(JWTBearer())])
def create_post(new_post: Post = Body()):

        db = Session()
        new_post = PostModel(**new_post.model_dump())
        db.add(new_post)
        db.commit()
        return JSONResponse(
            content={"message": "Post created successfully", "data": new_post.model_dump()},
            status_code=201      
        )
