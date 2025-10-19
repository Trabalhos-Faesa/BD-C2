from typing import Annotated, Optional

from pydantic import AfterValidator, BaseModel

class pedidoi(BaseModel):
    id_pedido: Optional[int] = None
    id_cliente: int
    data_pedido: Optional[str] = None
    status: str
    id_carrinho: int
    valorTotal: float