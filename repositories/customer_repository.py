from sqlalchemy.orm import Session

from models.customers_model import Customers


def get_customer_by_id(db: Session, customer_id : int):

      return db.query(Customers).filter(Customers.customer_id == customer_id).first()

def get_customer_by_mobile_number(db : Session, mobile_number : str):

    return db.query(Customers).filter(Customers.mobile_number == mobile_number).first()

