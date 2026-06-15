from pydantic import BaseModel, EmailStr, Field


class MemberCreate(BaseModel):

    name: str

    age: int = Field(
        gt=15
    )

    phone: str

    email: EmailStr

    membership_type: str


class MemberResponse(MemberCreate):

    id: int

    class Config:
        from_attributes = True
