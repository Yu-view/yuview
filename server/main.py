import crochet
crochet.setup()
from typing import Optional, Union
from unittest import signals
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from listings.spiders.shopee import ShopeeSpider


app = FastAPI()

origins = []

crawl_runner = CrawlerRunner()

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
    return 

@app.get("/sentiment/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return

def scrape_with_crochet():
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)

    eventual = crawl_runner.crawl(ShopeeSpider)
    return eventual

def _crawler_result(item, response, spider):
    return