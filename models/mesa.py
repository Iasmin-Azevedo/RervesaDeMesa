from pydantic import BaseModel

class QuadraCreate(BaseModel):
    tipo: str  # Pode ser 'beach-tenis', 'volei' ou 'futsal'
    capacidade: int  # Capacidade da quadra

    class Config:
        from_attributes = True
