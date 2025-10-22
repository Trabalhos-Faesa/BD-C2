from pydantic import BaseModel, EmailStr


class LoginPayload(BaseModel):
    email: EmailStr
    senha: str


class LoginSuccess(BaseModel):
    id_cliente: int
    email: EmailStr
    nome: str
    sobrenome: str
    msg: str = "Login realizado com sucesso!"
