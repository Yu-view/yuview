from ast import For
from calendar import c
from enum import unique
from operator import index
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Float
from sqlalchemy.orm import relationship

from .database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")


QueryListing = Table(
    "QueryListing",
    Base.metadata,
    Column("query_id", ForeignKey("query.id")),
    Column("listing_id", ForeignKey("listing.id")),
)

class Query(Base):
    __tablename__ = "query"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    term = Column(String, index=True)
    frequency = Column(Integer)

    #Bidirectional
    listings = relationship("Listing", secondary = QueryListing, back_populates="queries")

class Listing(Base):
    __tablename__ = "listing"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    rating = Column(Float)
    price = Column(Float)
    num_rating = Column(Integer)
    num_sold = Column(Integer)
    shop_id = Column(Integer, index=True)
    item_id = Column(Integer, unique=True)

    #Children
    reviews = relationship("Review", back_populates="listing")
    #Bidirectional
    queries = relationship("Query", secondary = QueryListing, back_populates="listings")

class Review(Base):
    __tablename__ = "review"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    model = Column(String, index=True)
    comment = Column(String, index=True, nullable=True)

    #Parent
    listing_id = Column(Integer, ForeignKey("listing.id"))