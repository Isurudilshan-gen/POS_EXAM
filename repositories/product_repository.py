from sqlalchemy.orm import Session

from models.product_model import Product


def get_product_by_id(db : Session, product_id : int):
    return db.query(Product).filter(Product.product_id == product_id).first()

def get_product_by_code(db: Session, product_code : int):
    return db.query(Product).filter(Product.product_code == product_code).first()

def get_all_products(db : Session):
    return db.query(Product).all()