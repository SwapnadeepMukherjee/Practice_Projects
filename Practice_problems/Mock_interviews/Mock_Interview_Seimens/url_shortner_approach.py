# Problem statement: 
# Design a scalable URL shortener service (like Bit.ly). The application should posses the following API's:

# 1. POST(/shorten) method: Accepts a long URL, returns a shortened URL.
# 2. GET(/{short_code}) method: Redirects to the original URL.
# 3. GET(/stats/{short_code}) method: Returns usage stats (number of hits, last accessed time, etc.)


# Swapnadeep's initial Approach:

# Input -> comes any url in any forms
# logic -> processs/mask the url and shorten it -> we will need to mask the url 
# logically ->

# how will we validate the uniques of the url such that it doesn't coincide with the other person's URL?

# Recursively validate the UUID before sharing the short-URL:

# original_url = ""
# list = [UUID, orig_url, short_url]

def post_long_url(self, original_url, list):
    original_url = ""
    list = [[UUID, orig_url, short_url]]

    for original_url in list[orig_url]:
        if original_url == list[orig_url]:
            return list[short_url]
        else:
            reuturn 0


# Swapandeep' AI approach with FastAPI:

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Dict
import hashlib
import base64
import string
import random

app = FastAPI()

# In-memory DB: short_code -> long_url
db: Dict[str, str] = {}

BASE_URL = "http://short.url/"  # Replace with real domain

class URLIn(BaseModel):
    long_url: str

class URLOut(BaseModel):
    short_url: str

def generate_short_code(long_url: str, length=6) -> str:
    """Generate a unique short code using a hash (for demo, can use random/base62)."""
    # Hash + base64 (collision risk is very low for demo; in prod will need to add check/retry or use DB ID)
    m = hashlib.md5(long_url.encode()).digest()
    b64 = base64.urlsafe_b64encode(m).decode()
    return b64[:length]

@app.post("/orig_url", response_model=URLOut)
def create_short_url(payload: URLIn):
    long_url = payload.long_url
    short_code = generate_short_code(long_url)
    # Uniqueness check; if collision, refine code:
    while short_code in db and db[short_code] != long_url:
        # If collision, use a random base62 string
        short_code = "".join(random.choices(string.ascii_letters + string.digits, k=6))
    db[short_code] = long_url
    return URLOut(short_url=BASE_URL + short_code)

@app.get("/{short_code}")
def resolve_short_url(short_code: str):
    if short_code not in db:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return {"long_url": db[short_code]}
    # Or, to redirect:
    # from fastapi.responses import RedirectResponse
    # return RedirectResponse(url=db[short_code])
