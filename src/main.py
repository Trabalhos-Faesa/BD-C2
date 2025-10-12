from fastapi import FastAPI, Request


app = FastAPI()


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/")
async def read_root(request: Request):  # request.scope
    return {"Hello": "World"}
