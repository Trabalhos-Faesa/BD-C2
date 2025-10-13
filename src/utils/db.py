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


async def main():
    sync_engine = get_engine()
    async_engine = get_async_engine()

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
