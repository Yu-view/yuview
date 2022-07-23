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

class ReviewBase(BaseModel):
    model: str
    comment: Union[str, None] = None


class QueryCreate(QueryBase):
    listings: list[ListingBase]

class Query(QueryBase):
    id: int

    class Config:
        orm_mode = True

class ListingCreate(ListingBase):
    reviews: list[ReviewBase] = []
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
    listing_id: int

    class Config:
        orm_mode = True
