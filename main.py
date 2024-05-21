from typing import Union
from db import Session, Quote, Base, engine
from sqlalchemy import select
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from random import randint, seed
import time

# Migration section
# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    author: str
    text: str


app = FastAPI()
seed(time.time())



def get_quote(quote_id):
    with Session.begin() as session:
        quote = session.scalar(select(Quote).where(Quote.id == quote_id))
        if quote:
            quote = Item(author=quote.author, text=quote.text)
        return quote
    
def limit():
    with Session.begin() as session:
        return session.query(Quote).count()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/quote/", response_model=Item)
@app.get("/quote/{item_id}", response_model=Item)
def read_item(item_id:int=-1):
    if item_id == -1:
        quote = get_quote(randint(0, limit()-1))
    else:
        quote = get_quote(item_id)
    print(f"{quote=}")
    if quote:
        return quote
    else:
        raise HTTPException(status_code=404, detail="Item not found")