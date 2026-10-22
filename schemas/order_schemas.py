from pydantic import BaseModel, Field


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int = Field(..., gt=0)

class OrderCreate(BaseModel):
    customer_mobile: str
    items: list[OrderItemCreate]