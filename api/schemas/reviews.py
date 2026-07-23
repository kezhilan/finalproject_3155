from typing import Optional
from pydantic import BaseModel


class ReviewBase(BaseModel):
    customer_id: int
    sandwich_id: int
    review_text: str
    rating: int


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    customer_id: Optional[int] = None
    sandwich_id: Optional[int] = None
    review_text: Optional[str] = None
    rating: Optional[int] = None


class Review(ReviewBase):
    id: int

    class ConfigDict:
        from_attributes = True