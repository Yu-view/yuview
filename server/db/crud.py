from sqlalchemy.orm import Session

from . import models
from api import schemas


def get_query(db: Session, query_id: int):
    return db.query(models.User).filter(models.Query.id == query_id).first()

def get_query_by_term(db: Session, term: str):
    return db.query(models.Query).filter(models.Query.term == term).first()

def get_listing(db: Session, listing_id: int):
    return db.query(models.Listing).filter(models.Listing.id == listing_id).first()

def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()


def create_query(db: Session, query: schemas.QueryCreate):
    db_query = models.Query(term = query.term)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
