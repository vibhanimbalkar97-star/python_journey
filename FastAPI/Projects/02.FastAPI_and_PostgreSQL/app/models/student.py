# Part 4: Create the StudentDB table
from app.database.connection import Base, engine
from sqlalchemy import String, Integer, Column

class StudentDB(Base):
    __tablename__ = "students_records"
    id      = Column(String    , primary_key=True)
    name    = Column(String(50), nullable=False) 
    age     = Column(Integer   , nullable=False)
    course  = Column(String(50), nullable=False)
    marks   = Column(Integer   , nullable=False)
    email   = Column(String    , unique=True, nullable=False)

Base.metadata.create_all(bind=engine)