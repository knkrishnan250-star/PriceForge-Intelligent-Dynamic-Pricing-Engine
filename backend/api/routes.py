from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database.db import SessionLocal
from backend.models.product_model import Product
from backend.core.pricing_engine import calculate_price
from backend.api.schemas import PriceRequest, PriceResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/calculate-price", response_model=PriceResponse)
def get_price(data: PriceRequest, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == data.product_id).first()

    if not product:
        return {"error": "Product not found"}

    optimized_price = calculate_price(
        product.base_price,
        data.demand_score,
        product.stock,
        data.current_hour
    )

    return PriceResponse(
        product_id=product.id,
        base_price=product.base_price,
        optimized_price=optimized_price
    )
