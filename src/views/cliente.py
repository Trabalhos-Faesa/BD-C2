from fastapi import APIRouter, HTTPException, status

from abstract import SQLResult, SQLResultDict, SQLResultStatus
from models.cliente import Cliente
from utils.db import aexec_query
from pydantic import BaseModel, EmailStr


router = APIRouter(prefix='/cliente', tags=['cliente'])


@router.get('/', response_model=SQLResult[Cliente])
async def read_all() -> SQLResultDict:
    return await aexec_query('cliente/read_all.sql')


@router.post('/', response_model=SQLResult[Cliente])
async def create(cliente: Cliente) -> SQLResultDict:
    return await aexec_query(
        'cliente/create.sql',
        cliente.model_dump()
    )


# Payload/response inline para evitar arquivo de modelo separado
class LoginPayload(BaseModel):
    email: EmailStr
    senha: str


class LoginSuccess(BaseModel):
    id_cliente: int
    email: EmailStr
    nome: str
    sobrenome: str
    msg: str = "Login realizado com sucesso!"


@router.post('/login', response_model=LoginSuccess)
async def login(credentials: LoginPayload) -> LoginSuccess:
    """
    Autentica um cliente no sistema.
    - **email**: Email do cliente
    - **senha**: Senha do cliente
    Retorna os dados do cliente se a autenticação for bem-sucedida.
    Lança HTTPException 401 se as credenciais forem inválidas.
    """
    result = await aexec_query(
        'cliente/login.sql',
        {'email': credentials.email}
    )


    if result['status'] == SQLResultStatus.ERROR or result['rowcount'] == 0:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos"
        )


    cliente_data = result['rows'][0]


    if cliente_data['senha'] != credentials.senha:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos"
        )

    return LoginSuccess(
        id_cliente=cliente_data['id_cliente'],
        email=cliente_data['email'],
        nome=cliente_data['nome'],
        sobrenome=cliente_data['sobrenome']
    )


@router.post('/cadastro', response_model=SQLResult[Cliente])
async def cadastrar(cliente: Cliente) -> SQLResultDict:
    """Endpoint alternativo para cadastro de cliente (alias de POST /cliente)."""
    return await aexec_query(
        'cliente/create.sql',
        cliente.model_dump()
    )
