from copyreg import constructor
import uvicorn
import crochet
crochet.setup()
from typing import Optional, Union
from scrapy import signals
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from sqlalchemy.orm import Session
from listings.spiders.shopee import ShopeeSpider
from db import models, database, crud
from . import schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

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


@app.post("/create_query/", response_model=schemas.Query)
async def create_query(query: schemas.QueryBase, db: Session = Depends(get_db)):
    def scrape_with_crochet(search: str):
        dispatcher.connect(_crawler_result, signal=signals.item_scraped)

        eventual = CrawlerRunner().crawl(ShopeeSpider, query = search)
        return eventual

    def _crawler_result(item, response, spider):
        data.append(dict(item))
    
    data = await scrape_with_crochet(search= query)
    reviews = await data['reviews']
    map(lambda x: schemas.ReviewCreate(model = x['model'], comment = x['comment']))
    map(lambda x: schemas.ListingCreate(title = x['name'], rating = x['rating'], price = x['price'], num_rating = x['num_rating'], num_sold = x['num_sold'], shop_id = x['shop_id'], item_id = x['item_id']))
    query = schemas.QueryCreate(term=query.term, listings=data)
    return crud.create_query(db, query=query)


@app.get("/read_query/", response_model=schemas.Query)
def read_query(query: str, db: Session = Depends(get_db)):
    db_query = crud.get_query_by_term(db, term=query)
    if db_query is None:
        raise HTTPException(status_code=400, detail="Not scraped")
    return db_query

@app.get("/read_query/{query_id}", response_model=schemas.Query)
def read_query_by_id(query_id: int, db: Session = Depends(get_db)):
    db_query = crud.get_query(db, query_id==query_id)
    return db_query
