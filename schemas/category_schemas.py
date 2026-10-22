from typing import Optional

from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):

    category_code : str = Field(...)
    category_name : str = Field(..., min_length=3, max_length=100)
    description : Optional[str] = Field(..., max_length=500)

class CategoryResponse(BaseModel):

    category_id: int
    category_code: str
    category_name: str
    description: Optional[str]
    active: bool

    class Config:
        from_attribute = True