from sqlalchemy.orm import Session

from models.order_model import Order


def get_order_by_id(db : Session, order_id : int):

       return db.query(Order).filter(Order.order_id == order_id).first()