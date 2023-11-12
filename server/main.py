from typing import Union
from fastapi import FastAPI
import api
import model_chatglm
from pydantic import BaseModel
import json

app = FastAPI()

class query(BaseModel):
    text: str
    _type: int # 0 for chat and 1 for observation
    history: str

@app.get("/")
def read_root():
    return "AssistX API!"

@app.get("/api/{api_key}")
def read_item(api_key: str, q: Union[query, None] = None):
    if not api.is_valid(api_key):
        return {"status":"error", "info":"Invalid key"}
    response, history = model_chatglm.chat(q.text, q._type, q.history)
    return {status"response":response, "history":json.dumps(history)}
    