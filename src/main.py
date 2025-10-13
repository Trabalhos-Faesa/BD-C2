from fastapi import FastAPI, Request
from fastapi.responses import ORJSONResponse

from views import management


app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(management.router)


@app.get("/")
async def read_root(request: Request):  # request.scope
    return {"Hello": "World"}
