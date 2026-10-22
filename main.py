from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import engine, Base
import models.category_model
from routers.item_router import router as item_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Exam API", version="1.0.0", docs_url="/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(item_router)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
