import requests
import json
import load_config
import tools.code_exec
history = "None"
def chat(msg):
    '''
class query(BaseModel):
    text: str
    _type: int # 0 for chat and 1 for observation
    history: str
    '''
    r = requests.post(
        load_config.api()+load_config.key(),
        data = {"text": msg, "_type": 0, "history": history}
    )
    res = json.loads(r.text)
    if res["status"]=="success":
        t = res["response"]
        # if t is a Dict, Lets call tools
        if type(t)==dict:
            if t.get()