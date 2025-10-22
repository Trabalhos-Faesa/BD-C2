from datetime import datetime
from typing import Annotated, Optional

from pydantic import BaseModel, Field


class Produto(BaseModel):
    id_produto: Optional[int] = None
    nome: Annotated[str, Field(min_length=1)]
    descricao: Optional[str] = None
    preco: Annotated[float, Field(ge=0)]
    quantidade_estoque: Annotated[int, Field(ge=0)] = 0
    categoria: Optional[str] = None
    data_criacao: Optional[datetime] = None
