import psycopg2
import traceback

try:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        user='app_user',
        password='app_password',
        database='app_db'
    )
    print("✅ Conexão OK com psycopg2")
    cur = conn.cursor()
    cur.execute("SELECT version()")
    print(cur.fetchone())
    conn.close()
except Exception as e:
    print(f"❌ Erro: {e}")
    traceback.print_exc()
