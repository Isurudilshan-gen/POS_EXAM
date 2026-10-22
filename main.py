from fastapi import FastAPI

from core.database import engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()
