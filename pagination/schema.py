from pydantic import BaseModel


class Comment(BaseModel):
    comment_id: int
    content: str
    author: str
    timestamp: int
    post_id: int


class Post(BaseModel):
    post_id: int
    content: str
    author: str
    timestamp: int
    comments: str

    class Config:
        orm_mode = True
