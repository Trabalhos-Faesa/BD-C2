from typing import Annotated, Optional

from pydantic import AfterValidator, BaseModel


class CarrinhoCompra(BaseModel):
    id_carrinho: Optional[int] = None
    id_cliente: int
    id_produto: int
    data_criacao: Optional[str] = None
    quantidade: Annotated[int, AfterValidator(lambda v: v if v > 0 else 1)]
