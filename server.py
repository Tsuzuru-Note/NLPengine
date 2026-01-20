from fastapi import FastAPI, Body
from engine import NLPEngine

# FIXME: Use for Server test
from tests.helloserver import helloServer

#Server TEST
hello_server = helloServer()

#The main NLP engine
engine = NLPEngine()

# Run http://server-path/
app = FastAPI()

@app.post("/hello/{msg}")
def hello_api(msg: str):
    result = hello_server.server(msg)
    return {"message": result}

@app.post("/nlpengine/")
async def nlpengine(data: dict = Body(...)):
    return {"received_data": data}