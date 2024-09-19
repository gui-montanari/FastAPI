from typing import Optional, List
from pydantic import BaseModel, EmailStr, ConfigDict

from schemas.artigo_schema import ArtigoSchema


class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: EmailStr
    eh_admin: bool = False

    model_config = {"from_attributes": True}

class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str

class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: List[ArtigoSchema] = []

class UsuarioSchemaUp(BaseModel):
    nome: Optional[str] = None
    sobrenome: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    eh_admin: Optional[bool] = None

    model_config = ConfigDict(from_attributes=True)