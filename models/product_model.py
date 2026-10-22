from sqlalchemy import Column, Integer, String, NUMERIC, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Product(Base):

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String, unique=True, nullable=False)
    product_name = Column(String, nullable=False)
    unit_price = Column(NUMERIC(15, 2), nullable=False )
    available_quantity = Column(Integer, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)

    categories = relationship("Category", back_populates="products")
