# Dependency Injection example in database:
# Source: Google

# Database Session as a Dependency:

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

# Database configuration
DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a database session
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Use in your path operations
app = FastAPI()

@app.post("/items/")
def create_item(item: str, db: Session = Depends(get_db)):
    # Use the 'db' session here
    db.add(YourModel(name=item))
    db.commit()
    db.refresh(item)
    return {"message": f"Item '{item}' created."}

# Settings as a Dependency

from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    database_url: str = "sqlite:///./default.db"
    debug_mode: bool = False

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

def get_settings():
    return AppSettings()

@app.get("/info/")
def get_app_info(settings: AppSettings = Depends(get_settings)):
    return {"database_url": settings.database_url, "debug_mode": settings.debug_mode}

# ---------------------------------------------------------------------------------|

# Example of raising a 400 in FastAPI:

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.post("/items/")
async def create_items(item_id: int, q: str = None):
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="Item ID must be a positive integer.")
    return {"item_id": item_id, "q": q}


# Example of a 422 in FastAPI (Pydantic validation):

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
async def create_item(item: Item):
    return item