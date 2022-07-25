import sqlalchemy
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Float, BigInteger
from sqlalchemy.dialects.postgresql import UUID
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
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("gen_random_uuid()"))
    term = Column(String, index=True)
    frequency = Column(Integer)

    #Bidirectional
    listings = relationship("Listing", secondary = QueryListing, back_populates="queries")

class Listing(Base):
    __tablename__ = "listing"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("gen_random_uuid()"))
    name = Column(String)
    rating = Column(Float)
    price = Column(Float)
    num_rating = Column(Integer)
    num_sold = Column(Integer)
    shop_id = Column(BigInteger)
    item_id = Column(BigInteger)

    #Bidirectional
    queries = relationship("Query", secondary = QueryListing, back_populates="listings")
    #Children
    reviews = relationship("Review")

class Review(Base):
    __tablename__ = "review"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=sqlalchemy.text("gen_random_uuid()"))
    model = Column(String, index=True)
    comment = Column(String, index=True, nullable=True)

    #Parent
    listing_id = Column(UUID(as_uuid=True), ForeignKey("listing.id"))