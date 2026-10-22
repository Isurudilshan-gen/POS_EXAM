from sqlalchemy.orm import Session

from models.category_model import Category


def get_category_by_id(db: Session, category_id: int):
    return db.query(Category).filter(Category.category_id == category_id).first()

def get_all_categories(db : Session):
    return db.query(Category).all()