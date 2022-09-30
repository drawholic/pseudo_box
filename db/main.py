from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///./db.db', echo=True)


SessionLocal = sessionmaker(bind=engine)

def get_db():
    s = SessionLocal()
    try:
        yield s
    finally:
        s.close()
