from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class Produto(BaseModel):
    id_produto: Optional[int] = None
    nome: str = Field(min_length=1)
    descricao: Optional[str] = None
    preco: float = Field(ge=0)
    quantidade_estoque: int = Field(ge=0)
    categoria: Optional[str] = None
    data_criacao: Optional[datetime] = None