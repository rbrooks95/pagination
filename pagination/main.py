# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from datetime import datetime
# from typing import List, Optional

# from fastapi_pagination import Page, add_pagination, paginate

import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import Post as SchemaPost
from schema import Comment as SchemaComment

from schema import Post
from schema import Comment

from models import Post as ModelPost
from models import Comment as ModelComment

import os
from dotenv import load_dotenv

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


# app = FastAPI()


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


@app.post("/post", response_model=SchemaPost)
async def create_post(post: SchemaPost):
    main_post = ModelPost(
        content=post.content,
        author=post.author,
        timestamp=post.timestamp,
        post_id=post.post_id,
        comment_id=post.comment_id,
    )
    db.session.add(main_post)
    db.session.commit()

    return main_post


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
