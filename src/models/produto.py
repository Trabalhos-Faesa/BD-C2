from typing import Annotated, Optional

from pydantic import AfterValidator, BaseModel


class Produto(BaseModel):
    id_produto: Optional[int] = None
    nome: str
    descricao: Optional[str] = None
    preco: float
    quantidade_estoque: Annotated[int, AfterValidator(lambda v: v if v >= 0 else 0)] = 0
    categoria: Optional[str] = None
