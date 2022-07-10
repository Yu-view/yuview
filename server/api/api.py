import uvicorn
import crochet
crochet.setup()
from typing import Optional, Union
from scrapy import signals
from fastapi import FastAPI, HTTPException, Depends
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

@app.get("/listings")
async def find_product(query: str):
    async def scrape_with_crochet(search: str):
        dispatcher.connect(_crawler_result, signal=signals.item_scraped)

        eventual = crawl_runner.crawl(ShopeeSpider, query = search)
        return eventual

    def _crawler_result(item, response, spider):
        data.append(dict(item))
    
    data = await scrape_with_crochet(search= query)
    return data

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/query/", response_model=schemas.Query)
def create_user(query: schemas.QueryCreate, db: Session = Depends(get_db)):
    return crud.create_query(db, query=query)


@app.get("/query/", response_model=schemas.User)
def read_query(query: str, db: Session = Depends(get_db)):
    db_query = crud.get_query_by_term(db, term=query)
    if db_query is None:
        raise HTTPException(status_code=400, detail="Not scraped")
    return db_query

@app.get("/query/{query_id}", response_model=schemas.Query)
def read_query_by_id(query_id: int, db: Session = Depends(get_db)):
    db_query = crud.get_query(db, query_id==query_id)
    return db_query



@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items