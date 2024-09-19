from typing import Optional
from pydantic import BaseModel, HttpUrl

class ArtigoSchemaBase(BaseModel):
    titulo: str
    descricao: str
    url_fonte: HttpUrl

class ArtigoSchemaCreate(ArtigoSchemaBase):
    pass

class ArtigoSchema(ArtigoSchemaBase):
    id: int
    usuario_id: int

    model_config = {"from_attributes": True}