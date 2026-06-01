from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class UsuarioBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    email: EmailStr

class UsuarioCreate(UsuarioBase):
    senha: str = Field(..., min_length=6)

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        from_attributes = True

class UsuarioAtualizarDadosSensiveis(BaseModel):
    email: Optional[EmailStr] = None
    senha: Optional[str] = Field(None, min_length=6)