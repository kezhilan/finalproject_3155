from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    customer_name: str
    email: str
    phone_number: str
    address: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    id: int

    class ConfigDict:
        from_attributes = True