import asyncio
from pathlib import Path
from typing import Any

import sqlalchemy.exc
from decouple import config
from sqlalchemy import (
    URL,
    CursorResult,
    Engine,
    create_engine,
    text,
)
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from abstract import SQLResultDict, SQLResultStatus
from utils.abstract import Singleton


DB_CONNECTION_STRING = config('DB_CONNECTION_STRING')


def error_response(msg: str) -> SQLResultDict:
    return {
        'rows': [],
        'rowcount': -1,
        'status': SQLResultStatus.ERROR,
        'msg': str(msg),
    }


def get_engine(
    connection_string: str | URL = DB_CONNECTION_STRING,
    *args,
    **kwargs,
) -> Engine:
    engine = create_engine(
        connection_string,
        *args,
        **kwargs
    )
    return engine


def get_async_engine(
    connection_string: str | URL = DB_CONNECTION_STRING,
    *args,
    **kwargs,
) -> AsyncEngine:
    engine = create_async_engine(
        connection_string,
        *args,
        **kwargs
    )
    return engine


# XXX: LRU cache over get_*engine is a batter way?
class DBEngines(metaclass=Singleton):
    def __init__(self) -> None:
        self.engine: Engine = get_engine()
        self.aengine: AsyncEngine = get_async_engine()


db_engines = DBEngines()
sync_engine = db_engines.engine
async_engine = db_engines.aengine


def get_query(sql_file: str) -> str:
    file_path = Path(__file__).parent / ('../sql/' + sql_file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return content
    except (FileNotFoundError, IsADirectoryError):
        raise ValueError('Erro ao carregar arquivo SQL! Verifique o nome.')
    except OSError:  # FileNotFoundError, IsADirectoryError, PermissionError, ...
        raise


def wrap_result(result: CursorResult) -> SQLResultDict:
    if result.returns_rows:
        rows = result.mappings().all()
    else:
        rows = []
    return {
        'rows': rows,  # type: ignore[typeddict-item]
        'rowcount': result.rowcount,
    }


def exec_query(
    sql_file: str,
    query_params: dict[str, Any] | None = None,
    engine: Engine = sync_engine,
) -> SQLResultDict:
    try:
        query_string = get_query(sql_file)
    except (ValueError, OSError) as err:
        response: SQLResultDict = error_response(str(err))
    try:
        with engine.begin() as conn:
            result = conn.execute(text(query_string), query_params)
            response = wrap_result(result)
        response.update({
            'status': SQLResultStatus.SUCCESS,
        })
    except sqlalchemy.exc.SQLAlchemyError as err:
        response = error_response(str(err))
    return response


async def main():
    """
    Cole o código de `utils.abstract.Singleton` nesse arquivo para testar a conn. com o DB executando diretamente
    Ou simplesmente execute `pytest -k 'TestDBEngines'`
    """
    sync_engine = DBEngines().engine
    async_engine = DBEngines().aengine

    print('[*] CONNECTION_STRING:')
    print(DB_CONNECTION_STRING)

    print()
    print('[*] For: Sync Engine')
    print('[*] Connecting...')
    with sync_engine.connect() as conn:
        query = 'SELECT 1;'
        # query = 'SELECT 1 WHERE 1=0;'
        if conn.execute(text(query)).fetchall():
            print('[+] Dados obtidos com sucesso!')
        else:
            print('[!] Nenhum dado obtido!')

    print()
    print('[*] For: Async Engine')
    print('[*] Connecting...')
    async with async_engine.connect() as conn:
        query = 'SELECT 1;'
        # query = 'SELECT 1 WHERE 1=0;'
        if (await conn.execute(text(query))).fetchall():
            print('[+] Dados obtidos com sucesso!')
        else:
            print('[!] Nenhum dado obtido!')


if __name__ == '__main__':
    asyncio.run(main())
