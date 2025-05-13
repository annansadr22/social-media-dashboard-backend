# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy database engine
engine = create_engine(
    DATABASE_URL
)

# Create a session for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# ✅ Dependency: Get database session (This remains here)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
