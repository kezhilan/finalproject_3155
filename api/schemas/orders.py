from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail
from .customers import Customer



class OrderBase(BaseModel):
    customer_id: int
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_name: Optional[str] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None

    customer: Customer = None
    order_details: list[OrderDetail] = None

    class ConfigDict:
        from_attributes = True