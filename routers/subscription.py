from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db

from models.subscription import Subscription

from schemas.subscription import SubscriptionCreate

router = APIRouter(
    prefix="/subscriptions",
    tags=["Subscriptions"]
)


@router.post("")
def create_subscription(
    subscription: SubscriptionCreate,
    db: Session = Depends(get_db)
):

    if subscription.end_date <= subscription.start_date:
        raise HTTPException(
            400,
            "End date must be greater than start date"
        )

    db_subscription = Subscription(
        **subscription.model_dump()
    )

    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)

    return db_subscription


@router.get("")
def get_subscriptions(
    db: Session = Depends(get_db)
):
    return db.query(Subscription).all()


@router.get("/{subscription_id}")
def get_subscription(
    subscription_id: int,
    db: Session = Depends(get_db)
):

    subscription = db.query(Subscription).filter(
        Subscription.id == subscription_id
    ).first()

    if not subscription:
        raise HTTPException(
            404,
            "Subscription not found"
        )

    return subscription
