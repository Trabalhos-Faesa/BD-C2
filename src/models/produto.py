from typing import Annotated, Optional

from pydantic import AfterValidator, BaseModel

class Produtos(BaseModel):
    id_produto: int
    nomeProduto: str
    descricao: str
    preco: float
    data_criacao: Optional[str] = None
    quantidade_estoque: Annotated[int, AfterValidator(lambda v: v if v >= 0 else 0)]
    categoria: str