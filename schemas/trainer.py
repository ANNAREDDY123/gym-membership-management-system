from pydantic import BaseModel


class TrainerCreate(BaseModel):

    name: str

    specialization: str

    experience: int


class TrainerResponse(TrainerCreate):

    id: int

    class Config:
        from_attributes = True
