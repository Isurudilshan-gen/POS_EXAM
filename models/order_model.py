from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Boolean, NUMERIC, false
from sqlalchemy.orm import relationship

from core.database import Base


class Order(Base):

    __tablename__ = "order"

    order_id = Column(Integer, nullable=False, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    order_date_time = Column(DateTime, server_default=func.now(), nullable=False)
    order_status = Column(Boolean, default="COMPLETED")
    total_amount = Column(NUMERIC(10, 2), nullable=False)
    loyalty_points_earned = Column(Integer, nullable=False)

    customer = relationship("Customer", backref="orders")
    items = relationship("OrderItem", backref="customer_order")


class OrderItem(Base):

    __tablename__ = "order_items"

    order_item_id = Column(Integer, nullable=False, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(NUMERIC(10, 2), nullable=False)
    subtotal = Column(NUMERIC(10, 2 ), nullable=False)

    customer_order = relationship("Order", backref="items")
