from typing import Union
from fastapi import FastAPI

from src.main_scraper import main as scraper


app = FastAPI()


@app.get("/")
def read_root():
    return {"status code": 200,
            "message": "ok"}


@app.get("/newsList/{site}")
def newsList(site:str = "detik"):
    if site == "detik":
        site = ["https://news.detik.com/indeks"]
    else:
        site = ["https://www.detik.com/edu/indeks"]

    data = scraper(site)
    return data
