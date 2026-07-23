from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
from .customers import Customer
from .promotions import Promotion



class OrderBase(BaseModel):
    customer_id: int
    tracking_number: str
    order_status: str
    total_price: float
    description: Optional[str] = None
    promotion_id: Optional[int] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None
    description: Optional[str] = None

class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None

    customer: Customer = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True