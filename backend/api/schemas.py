from pydantic import BaseModel

class PriceRequest(BaseModel):
    product_id: int
    demand_score: int
    current_hour: int

class PriceResponse(BaseModel):
    product_id: int
    base_price: float
    optimized_price: float
