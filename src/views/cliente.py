from fastapi import APIRouter

from abstract import SQLResult, SQLResultDict
from models.cliente import Cliente
from utils.db import exec_query


router = APIRouter(prefix='/cliente', tags=['cliente'])


@router.get('/', response_model=SQLResult[Cliente])
async def read_all() -> SQLResultDict:
    return exec_query('cliente/read_all.sql')


@router.post('/', response_model=SQLResult[Cliente])
async def create(cliente: Cliente) -> SQLResultDict:
    return exec_query(
        'cliente/create.sql',
        cliente.model_dump()
    )
