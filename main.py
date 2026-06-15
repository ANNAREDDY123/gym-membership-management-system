from fastapi import FastAPI

from database import engine, Base

from models.user import User
from models.member import Member
from models.trainer import Trainer
from models.subscription import Subscription

from routers.auth import router as auth_router
from routers.member import router as member_router
from routers.trainer import router as trainer_router
from routers.subscription import router as subscription_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gym Membership Management System"
)

app.include_router(auth_router)
app.include_router(member_router)
app.include_router(trainer_router)
app.include_router(subscription_router)
