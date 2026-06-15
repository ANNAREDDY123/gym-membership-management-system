from sqlalchemy import (
    Column,
    Integer,
    String
)

from database import Base


class Trainer(Base):
    __tablename__ = "trainers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    specialization = Column(String)

    experience = Column(Integer)
