from pydantic import BaseModel


class MesaCreate(BaseModel):
    nome: str
    localizacao: str
    tipo: str 

    class Config:
        from_attributes = True
