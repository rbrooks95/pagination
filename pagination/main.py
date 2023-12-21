# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from datetime import datetime
# from typing import List, Optional

# from fastapi_pagination import Page, add_pagination, paginate

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schema
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# class Comment(BaseModel):
#     comment_id: int
#     content: str
#     author: str
#     timestamp: datetime
#     post_id: int


# class Post(BaseModel):
#     post_id: int
#     content: str
#     author: str
#     timestamp: datetime
#     comments: Optional[List[Comment]] = None


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# //////////////////////////////////////////////////////////////////


@app.post("/post", response_model=schema.Post)
async def create_post(post: schema.Post, db: Session = Depends(get_db)):
    db_Post = crud.create_post(db, post)
    if db_Post:
        raise HTTPException(status_code=400, detail="post nit created")
    return crud.create_post(db=db, post=db_Post)


@app.get("/post/{user_id}/{post_id}")
async def get_post(user_id: int, post_id: int):
    return {"message": "Post fetched", "post_id": post_id}


@app.put("/post/{user_id}/{post_comment_id}")
async def update_post(user_id: int, post_comment_id: int, post: Post):
    return {"message": "Post updated", "post_id": post_comment_id}


@app.delete("/post/{user_id}/{delete_comment_id}")
async def delete_post_or_comment(user_id: int, delete_comment_id: int):
    return {"message": "Post or Comment deleted", "id": delete_comment_id}


@app.get("/api/posts/{post_id}/comments")
async def get_post_comments(post_id: int, page: int = 1, limit: int = 10):
    # right here might need some assitance with pagination
    return {"message": "Comments fetched", "post_id": post_id}


def main():
    pass


if __name__ == "__main__":
    main()
