from typing import Optional

from pydantic import BaseModel


class pedido(BaseModel):
    id_pedido: Optional[int] = None
    id_cliente: int
    data_pedido: Optional[str] = None
    status: str
    id_carrinho: int
    valorTotal: float
