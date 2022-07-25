from importlib.resources import read_text
import sys, os
from typing import Optional, Union
from urllib import response
from uuid import UUID
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, Response, status
from fastapi.middleware.cors import CORSMiddleware
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sqlalchemy.orm import Session
from twisted.internet import reactor
from listings.spiders.shopee import ShopeeSpider
from db import models, database, crud
from . import schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# if "twisted.internet.reactor" in sys.modules:
    # del sys.modules["twisted.internet.reactor"]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}


# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/scrape_query/")
def create_query(query: str, db: Session = Depends(get_db)):
    os.system(f"scrapy crawl shopee -a query={query}")
    return {"Status": "Scraped"}


@app.get("/find_query/", response_model=schemas.Query)
def read_query(query: str, bt: BackgroundTasks, response: Response, db: Session = Depends(get_db)):
    db_query = crud.get_query_by_term(db, term=query)
    if db_query is None:
        raise HTTPException(status_code=400, detail="Not scraped")
    return db_query

# @app.get("/find_query/{query_id}",  response_model=schemas.Query)
# def read_query_by_id(query_id: UUID, db: Session = Depends(get_db)):
#     db_query = crud.get_query(db, query_id==query_id)
#     return db_query

@app.get("/get_listing/{listing_id}", response_model=schemas.Listing)
def get_listing(listing_id: UUID, db: Session = Depends(get_db)):
    db_listing = crud.get_listing(db, listing_id= listing_id)
    return db_listing

# @app.put("/run_summary/")
# def run_summary(query_id: UUID, db: Session = Depends(get_db)):
#     listings = crud.get_listings_by_query(db, query_id=query_id)
#     for listing in listings:
#         reviews = crud.get_reviews_by_listing(db, listing_id=listing.id)
#         listing.summary.append(nlp(reviews))
#     return listings