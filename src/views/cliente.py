from fastapi import APIRouter

from abstract import SQLResult, SQLResultDict
from models.cliente import Cliente
from utils.db import aexec_query


router = APIRouter(prefix='/cliente', tags=['cliente'])


@router.post('/', response_model=SQLResult[Cliente])
async def create(cliente: Cliente) -> SQLResultDict:
    return await aexec_query(
        'cliente/create.sql',
        cliente.model_dump(),
    )


@router.get('/', response_model=SQLResult[Cliente])
async def read_all() -> SQLResultDict:
    return await aexec_query('cliente/read_all.sql')


@router.get('/{id_cliente}', response_model=SQLResult[Cliente])
async def read_one(id_cliente: int) -> SQLResultDict:
    return await aexec_query(
        'cliente/read_one.sql',
        {
            'id_cliente': id_cliente,
        },
    )
