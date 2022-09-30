from fastapi import FastAPI
from db.main import engine
from db.models import Base
from users.main import router

Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(router)
