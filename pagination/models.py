from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    comment_id = Column(String)
    content = Column(String)
    author = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    post_id = Column(Integer, ForeignKey("post.id"))


class Post(Base):
    __tabelname__ = "post"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    content = Column(String)
    author = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    comments = Column(String)
