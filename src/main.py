from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from abstract import SQLResult, SQLResultStatus
from views import management, cliente, carrinho, account, produto


app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(management.router)
app.include_router(cliente.router)
app.include_router(carrinho.router)
app.include_router(account.router)
app.include_router(produto.router)


@app.get("/")
async def root(request: Request, response_model=SQLResult):
    # request.scope
    return {
        'rows': [],
        'rowcount': -1,
        'status': SQLResultStatus.SUCCESS,
        'msg': "Welcome!",
    }