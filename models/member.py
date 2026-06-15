from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from database import Base


class Member(Base):
    __tablename__ = "members"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String)

    age = Column(Integer)

    phone = Column(String)

    email = Column(
        String,
        unique=True
    )

    membership_type = Column(String)

    trainer_id = Column(
        Integer,
        ForeignKey("trainers.id"),
        nullable=True
    )
