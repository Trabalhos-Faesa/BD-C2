from fastapi import APIRouter

from abstract import SQLResult, SQLResultDict
from utils.db import exec_query


router = APIRouter(prefix='/cliente', tags=['cliente'])


@router.get('/', response_model=SQLResult)
async def read_all() -> SQLResultDict:
    return exec_query('cliente/read_all.sql')
