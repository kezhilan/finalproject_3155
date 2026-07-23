from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    card_last_four = Column(String(4), nullable=True)
    transaction_status = Column(String(50), nullable=False)
    payment_type = Column(String(50), nullable=False)
    order = relationship("Order", back_populates="payment")