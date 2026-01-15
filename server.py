from fastapi import FastAPI
import uvicorn

# FIXME: Use for Server test
from tests.helloserver import helloServer
hello_server = helloServer()

app = FastAPI() # Run http://server-path/

@app.post("/hello/{msg}")
def hello_api(msg: str):
    result = hello_server.server(msg)
    return {"message": result}