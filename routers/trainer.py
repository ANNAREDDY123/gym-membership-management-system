from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.trainer import Trainer
from models.member import Member

from schemas.trainer import TrainerCreate

router = APIRouter(
    prefix="/trainers",
    tags=["Trainers"]
)


@router.post("")
def create_trainer(
    trainer: TrainerCreate,
    db: Session = Depends(get_db)
):

    db_trainer = Trainer(
        name=trainer.name,
        specialization=trainer.specialization,
        experience=trainer.experience
    )

    db.add(db_trainer)
    db.commit()
    db.refresh(db_trainer)

    return db_trainer


@router.get("")
def get_trainers(
    db: Session = Depends(get_db)
):
    return db.query(Trainer).all()


@router.put("/{trainer_id}")
def update_trainer(
    trainer_id: int,
    trainer: TrainerCreate,
    db: Session = Depends(get_db)
):

    db_trainer = db.query(Trainer).filter(
        Trainer.id == trainer_id
    ).first()

    if not db_trainer:
        raise HTTPException(
            404,
            "Trainer not found"
        )

    db_trainer.name = trainer.name
    db_trainer.specialization = trainer.specialization
    db_trainer.experience = trainer.experience

    db.commit()

    return {"message": "Trainer updated"}


@router.delete("/{trainer_id}")
def delete_trainer(
    trainer_id: int,
    db: Session = Depends(get_db)
):

    trainer = db.query(Trainer).filter(
        Trainer.id == trainer_id
    ).first()

    if not trainer:
        raise HTTPException(
            404,
            "Trainer not found"
        )

    db.delete(trainer)
    db.commit()

    return {"message": "Trainer deleted"}


@router.post("/{trainer_id}/members/{member_id}")
def assign_trainer(
    trainer_id: int,
    member_id: int,
    db: Session = Depends(get_db)
):

    trainer = db.query(Trainer).filter(
        Trainer.id == trainer_id
    ).first()

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not trainer:
        raise HTTPException(
            404,
            "Trainer not found"
        )

    if not member:
        raise HTTPException(
            404,
            "Member not found"
        )

    member.trainer_id = trainer_id

    db.commit()

    return {
        "message":
        "Trainer assigned"
    }


@router.get("/{trainer_id}/members")
def trainer_members(
    trainer_id: int,
    db: Session = Depends(get_db)
):

    return db.query(Member).filter(
        Member.trainer_id == trainer_id
    ).all()
