import os
from typing import Optional

from config.server import app

from constants.api_keys import APIKey


@app.get("/")
def home():
    return {APIKey.MESSAGE: f"Arukou Loaded and Serving for {os.environ.get('ENVIRONMENT')} environment!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q
    }
