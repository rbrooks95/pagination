from sqlalchemy.orm import Session
from . import models, schema


def get_post(db: Session, user_id: int):
    return db.query(models.Post).filter(models.User.id == user_id).first()


def get_comment(db: Session, user_id: int):
    return db.query(models.Comment).filter(models.Comment.id == user_id).first()


def create_post(db: Session, post: schema.Post.Create):
    db_post = models.Post(
        post_id=post.post_id,
        content=post.content,
        author=post.author,
        timestamp=post.created_at,
        comments=post.comments,
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
