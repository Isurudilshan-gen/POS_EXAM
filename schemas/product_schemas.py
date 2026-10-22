import decimal

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):

    product_code : str = Field(..., min_length=1)
    product_name : str = Field(..., min_length=3)
    unit_price : float = Field(..., ge=0)
    available_quantity : int = Field(..., ge=0)
    active : bool = Field(...)
    category_id : int = Field(...)

class ProductResponse(BaseModel):

    product_id : int
    product_code: str
    product_name: str
    unit_price: float
    available_quantity: int
    active: bool
    category_id: int

    class Config:
        from_attribute = True