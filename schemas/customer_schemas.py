from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class CustomerCreate(BaseModel):

    mobile_number : str = Field(...)
    fullname : str = Field(..., min_length=3, max_length=100)
    email : str = Field(...)

    @field_validator("mobile_number")
    def number_validator(self, num : str) -> ValueError | str:
        if num[:1] == "07":
            num = "+94" + num[1:]
        elif num[:1] == "+94":
            pass
        else:
            return ValueError("Invalid Phone number Format")
        return num

class CustomerResponse(BaseModel):

    customer_id: int
    mobile_number: str
    full_name: str
    email:Optional[str]
    loyalty_points: int
    registered_at: datetime

    class Config:
        from_attributes = True
