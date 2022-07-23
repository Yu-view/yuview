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
    db_query = models.Query(term = query.term, frequence = 1, listings = query.listings)
    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query
