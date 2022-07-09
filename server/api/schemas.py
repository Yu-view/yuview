from datetime import datetime
from typing import Union

from pydantic import BaseModel


class QueryBase(BaseModel):
    term: str


class QueryCreate(QueryBase):
    time: datetime


class Query(QueryBase):
    id: int
    listings: list[Listing]

    class Config:
        orm_mode = True


class ListingBase(BaseModel):
    title: str
    rating: float
    price: float
    num_rating: int
    num_sold: int
    shop_id: int
    item_id: int
    queries: list[Query]

class ListingCreate(ListingBase):
    pass


class Listing(ListingBase):
    id: int
    reviews: list[Review] = []

    class Config:
        orm_mode = True

class ReviewBase(BaseModel):
    model: str
    comment: Union[str, None] = None
    listing_id: int
    listing: Listing

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True