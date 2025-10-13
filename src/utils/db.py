import asyncio

from decouple import config
from sqlalchemy import (
    URL,
    Engine,
    create_engine,
    text,
)
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from utils.abstract import Singleton


DB_CONNECTION_STRING = config('DB_CONNECTION_STRING')


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
    def __init__(
        self,
        engine_args=[],
        engine_kwargs={},
        aengine_args=[],
        aengine_kwargs={},
    ) -> None:
        self.engine: Engine = get_engine(*engine_args, **engine_kwargs)
        self.aengine: AsyncEngine = get_async_engine(*aengine_args, **aengine_kwargs)


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
