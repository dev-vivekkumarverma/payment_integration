from database import Base
from sqlalchemy import create_engine, Column, Integer, String, Float
class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    amount = Column(Float)
    payment_id = Column(String, unique=True, index=True)
    status = Column(String)
