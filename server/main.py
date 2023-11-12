from typing import Union
from fastapi import FastAPI
import api
import model_chatglm

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/{api_key}")
def read_item(api_key: str, q: Union[str, None] = None):
    if api.is_valid(api_key):

    