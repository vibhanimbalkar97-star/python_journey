# Part 7: get_db() - one session per request
#Opens a session, gives it to the endpoint, always closes it, replaces load_data/save_data

# Opens a session, pauses at yield while the endpoint doest its work and once the endpoint completed it's work the session will be closed.

from app.database.connection import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()