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
    # a doc of this api
    return "AssistX API!\n"

@app.get("/add_key/{token}/{key}")
def read_root(token: str, key: str):
    if token != "token":
        return {"status":"error", "info":"Invalid token"}
    api.add_key(key)
    return {"status":"success"}

@app.get("/api/{api_key}")
def core(api_key: str, q: Union[query, None] = None):
    if not api.is_valid(api_key):
        return {"status":"error", "info":"Invalid key"}
    response, history = model_chatglm.chat(q.text, q._type, q.history)
    return {"status":"success", "response":response, "history":json.dumps(history)}
    