from pydantic import BaseModel

class ReservaCreate(BaseModel):
    mesa_id: int
    data: str
    hora: str
    cliente: str

    class Config:
        from_attributes = True