from pydantic import BaseModel
from datetime import date


class SubscriptionCreate(BaseModel):

    member_id: int

    start_date: date

    end_date: date

    amount: float

    status: str


class SubscriptionResponse(SubscriptionCreate):

    id: int

    class Config:
        from_attributes = True
