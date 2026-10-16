from sqlalchemy.orm import Session

from database import models
import schemas


def get_authors(db: Session, skip: int, limit: int):
    return db.query(models.DBAuthor).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.DBAuthor(**author.model_dump())

    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def get_author_detail(db: Session, author_id: int):
    return db.query(models.DBAuthor).filter(models.DBAuthor.id == author_id).first()
