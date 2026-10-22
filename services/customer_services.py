from starlette.exceptions import HTTPException

from repositories import customer_repository


def get_customer_by_mobile(db, mobile_number: str):
    customer = customer_repository.get_customer_by_mobile_number(db, mobile_number)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer