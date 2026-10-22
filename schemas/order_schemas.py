from datetime import datetime
from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderItemResponse(BaseModel):

    order_item_id: int
    order_id : int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    customer_mobile: str
    items: list[OrderItemCreate]

class OrderResponse(BaseModel):

    order_id: int
    customer_id: int
    order_date_time: datetime
    order_status: str
    total_amount: float
    loyalty_points_earned: int
    items: list[OrderItemResponse]

    class Config:
        from_attributes = True

