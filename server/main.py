from typing import Union
from fastapi import FastAPI
import api
import model_chatglm
from pydantic import BaseModel

app = FastAPI()

class query(BaseModel):
    text: str
    _type: int #
    history: str
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/{api_key}")
def read_item(api_key: str, q: Union[query, None] = None):
    if not api.is_valid(api_key):
        return {"status":"error", "info":"Invalid key"}
    return model_chatglm.chat(q.text, q._type, query.history)
    