from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import run_rag

app = FastAPI()


class QueryRequest(BaseModel):

    query: str


@app.post("/ask")

def ask_question(req: QueryRequest):

    result = run_rag(req.query)

    return result