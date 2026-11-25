from fastapi import FastAPI
from app.database.connection import engine, Base
from app.routers import student 



# Part 8: Create the FastAPI app
app = FastAPI()

# Part 4: Create database tables
Base.metadata.create_all(bind=engine)

# Register student routes
app.include_router(student.router)