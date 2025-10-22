from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from abstract import SQLResult, SQLResultStatus
import views


app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(views.management.router)
app.include_router(views.cliente.router)
app.include_router(views.carrinho.router)
app.include_router(views.produto.router)
app.include_router(views.relatorios.router)


@app.get("/")
async def root(request: Request, response_model=SQLResult):
    # request.scope
    return {
        'rows': [],
        'rowcount': -1,
        'status': SQLResultStatus.SUCCESS,
        'msg': "Welcome!",
    }
