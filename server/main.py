import uvicorn
import crochet
crochet.setup()
from typing import Optional, Union
from scrapy import signals
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
from listings.spiders.shopee import ShopeeSpider


app = FastAPI()

origins = ["*"]

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
    async def scrape_with_crochet(search: str):
        dispatcher.connect(_crawler_result, signal=signals.item_scraped)

        eventual = crawl_runner.crawl(ShopeeSpider, query = search)
        return eventual

    def _crawler_result(item, response, spider):
        data.append(dict(item))
    
    data = await scrape_with_crochet(search= query)
    return data

@app.get("/sentiment/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)