from uuid import UUID
from sqlalchemy.orm import Session

from . import models
from api import schemas

def get_query(db: Session, query_id: UUID):
    return db.query(models.Query).filter(models.Query.id == query_id).first()

def get_query_by_term(db: Session, term: str):
    return db.query(models.Query).filter(models.Query.term == term).first()

def get_listing(db: Session, listing_id: UUID):
    return db.query(models.Listing).filter(models.Listing.id == listing_id).first()

def get_listings_by_query(db: Session, query_id: UUID):
    return db.query(models.Listing).filter(models.Listing.queries.any(id=query_id)).all()

def get_review(db: Session, review_id: int):
    return db.query(models.Review).filter(models.Review.id == review_id).first()

def get_reviews_by_listing(db: Session, listing_id: UUID):
    return db.query(models.Review).filter(models.Review.listing_id == listing_id).all()

def create_query(db: Session, query: schemas.QueryCreate):
    db_query = models.Query(term = query.term, frequency = 1)
    for listing in query.listings:
        db_listing = models.Listing(name = listing.name, rating = listing.rating, price = listing.rating, num_rating = listing.num_rating, num_sold = listing.num_sold, item_id = listing.item_id, shop_id = listing.shop_id)
        for review in listing.reviews:
            db_review = models.Review(model = review.model, comment = review.comment)
            db_listing.reviews.append(db_review)
        db_listing.queries.append(db_query)
        db_query.listings.append(db_listing)
        db.add(db_listing)

    db.add(db_query)
    db.commit()
    db.refresh(db_query)
    return db_query

def create_listing(db: Session, listing: schemas.ListingCreate):
    db_listing = models.Listing(name = listing.name, rating = listing.rating, price = listing.rating, num_rating = listing.num_rating, num_sold = listing.num_sold, item_id = listing.item_id, shop_id = listing.shop_id, queries = listing.queries)
    db.add(db_listing)
    db.commit()
    db.refresh(db_listing)
    return db_listing

def create_review(db: Session, review: schemas.ReviewCreate):
    db_review = models.Review(model = review.model, comment = review.comment)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review