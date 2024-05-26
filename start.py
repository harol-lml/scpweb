from typing import Union
from fastapi import FastAPI
from sele import scrapWeb

app = FastAPI()


@app.get("/")
def read_root():
    data = scrapWeb.get_web()
    return data


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}