from fastapi import FastAPI
from backend.database.db import Base, engine
from backend.api.routes import router

app = FastAPI(title="PriceForge Dynamic Pricing Engine")

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "PriceForge API Running 🚀"}
