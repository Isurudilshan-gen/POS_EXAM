from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.database import Base


class Category(Base):

    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, index=True, nullable=True)
    category_code = Column(String, unique=True, nullable=False)
    category_name = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    active = Column(Boolean, default=True, nullable=False)

    products = relationship("Product", backref="categories")











































#
# from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
# from sqlalchemy.sql import func
# from core.database import Base
#
# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100), nullable=False, index=True)
#     description = Column(String(255), nullable=True)
#     price = Column(Float, nullable=False)
#     is_available = Column(Boolean, default=True)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
