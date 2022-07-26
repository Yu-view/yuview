from datetime import datetime
from typing import List, Union
from uuid import UUID
from pydantic import BaseModel


class QueryBase(BaseModel):
    term: str


class ListingBase(BaseModel):
    name: str
    rating: float
    price: float
    num_rating: int
    num_sold: int
    item_id: int
    shop_id: int


class ReviewBase(BaseModel):
    comment: Union[str, None] = None


class ReviewCreate(ReviewBase):
    model: list[Union[str, None]]
    pass


class ListingCreate(ListingBase):
    reviews: list[ReviewCreate] = []
    queries = list[QueryBase]
    pass


class QueryCreate(QueryBase):
    listings: list[ListingCreate]
    pass


class Review(ReviewBase):
    id: UUID
    model: Union[str, None] = None
    listing_id: UUID

    class Config:
        orm_mode = True


class Listing(ListingBase):
    id: UUID
    summary: Union[str, None] = None

    class Config:
        orm_mode = True


class Query(QueryBase):
    id: UUID

    class Config:
        orm_mode = True
