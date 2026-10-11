
from fastapi import FastAPI

from database import get_all_products

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Simple Shop"}


@app.get("/products")
def products():
    return get_all_products()
