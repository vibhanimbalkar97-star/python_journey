# Part 2: Create the engine (connection to PostgreSQL)
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
with engine.connect() as conn:
    version = conn.execute(text("SELECT version()")).scalar()
    # print(f"Connect to the {version.split(",")[0]}")
    

# Part 3: Create SessionLocal and Base
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass