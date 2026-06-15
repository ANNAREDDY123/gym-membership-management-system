from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models.member import Member
from schemas.member import MemberCreate

router = APIRouter(
    prefix="/members",
    tags=["Members"]
)


@router.post("")
def create_member(
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    existing = db.query(Member).filter(
        Member.email == member.email
    ).first()

    if existing:
        raise HTTPException(
            400,
            "Email already exists"
        )

    db_member = Member(**member.model_dump())

    db.add(db_member)
    db.commit()
    db.refresh(db_member)

    return db_member


@router.get("")
def get_members(
    db: Session = Depends(get_db)
):
    return db.query(Member).all()


@router.get("/{member_id}")
def get_member(
    member_id: int,
    db: Session = Depends(get_db)
):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:
        raise HTTPException(
            404,
            "Member not found"
        )

    return member


@router.put("/{member_id}")
def update_member(
    member_id: int,
    member: MemberCreate,
    db: Session = Depends(get_db)
):

    db_member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not db_member:
        raise HTTPException(
            404,
            "Member not found"
        )

    db_member.name = member.name
    db_member.age = member.age
    db_member.phone = member.phone
    db_member.email = member.email
    db_member.membership_type = member.membership_type

    db.commit()

    return {"message": "Member updated"}


@router.delete("/{member_id}")
def delete_member(
    member_id: int,
    db: Session = Depends(get_db)
):

    member = db.query(Member).filter(
        Member.id == member_id
    ).first()

    if not member:
        raise HTTPException(
            404,
            "Member not found"
        )

    db.delete(member)
    db.commit()

    return {"message": "Member deleted"}
