import asyncio
import sys
sys.path.insert(0, 'src')

from decouple import config
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

async def test():
    DB_CONNECTION_STRING = config('DB_CONNECTION_STRING')
    print(f"Connection string: {DB_CONNECTION_STRING}")
    
    engine = create_async_engine(DB_CONNECTION_STRING, echo=True)
    
    try:
        async with engine.begin() as conn:
            result = await conn.execute(text("SELECT 1 as num"))
            row = result.fetchone()
            print("✅ Conexão OK:", row)
    except Exception as e:
        print("❌ Erro:", type(e), e)
        import traceback
        traceback.print_exc()
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(test())
