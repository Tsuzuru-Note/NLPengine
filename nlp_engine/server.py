from fastapi import FastAPI, Body, HTTPException
from .engine import NLPEngine

#The main NLP engine
engine = NLPEngine()

# Run http://server-path/
app = FastAPI()

@app.post("/nlpengine/")
async def nlpengine(data: dict = Body(...)):
    text = data.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="Bad Request...")

    engine.analyze(text)
    return engine.get_sentences()
