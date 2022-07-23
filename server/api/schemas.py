from datetime import datetime
from typing import Union

from pydantic import BaseModel


class QueryBase(BaseModel):
    term: str


class ListingBase(BaseModel):
    title: str
    rating: float
    price: float
    num_rating: int
    num_sold: int
    shop_id: int
    item_id: int
    queries: list[QueryBase]


class ReviewBase(BaseModel):
    model: str
    comment: Union[str, None] = None
    listing_id: int
    listing: ListingBase


class QueryCreate(QueryBase):
    time: datetime


class Query(QueryBase):
    id: int
    listings: list[ListingBase]

    class Config:
        orm_mode = True


class ListingCreate(ListingBase):
    pass


class Listing(ListingBase):
    id: int
    reviews: list[ReviewBase] = []

    class Config:
        orm_mode = True


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True
