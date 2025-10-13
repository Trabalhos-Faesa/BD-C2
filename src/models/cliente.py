from typing import Annotated

from pydantic import AfterValidator, BaseModel, EmailStr, StringConstraints

from utils.validators import valid_cpf, valid_senha


class Cliente(BaseModel):
    id: int
    email: EmailStr
    senha: Annotated[str, AfterValidator(valid_senha)]
    nome: str
    sobrenome: str
    cpf: Annotated[str, AfterValidator(valid_cpf)]
    # Endereço:
    cep: Annotated[str, StringConstraints(min_length=8, max_length=8)]
    uf: str  # Unidade Federativa (Estado)
    cidade: str
    bairro: str
    rua: str
    numero: str
    complemento: str
