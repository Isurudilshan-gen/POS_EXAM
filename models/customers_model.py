from sqlalchemy import Column, Integer, String, DateTime, func

from core.database import Base


class Customers(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, nullable=False, unique=True, index=True, primary_key=True)
    mobile_number = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    loyalty_points = Column(Integer, default=0, nullable=False)
    registered_at = Column(DateTime, server_default=func.now(), nullable=False)

