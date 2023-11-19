import requests
import json
import core.load_config
import core.tools.code_exec

history = "None"

def chat(msg):
    global history
    '''
class query(BaseModel):
    text: str
    _type: int # 0 for chat and 1 for observation
    history: str
    '''
    r = requests.post(
        core.load_config.api()+core.load_config.key(),
        data = json.dumps({"text": msg, "t": 0, "history": history})
    )
    print(r.text)
    res = json.loads(r.text)
    history = json.dumps(res["history"])
    if res["status"]=="success":
        t = res["response"]
        # if t is a Dict, Lets call tools
        while type(t)==dict:
            if t.get("name") == "code-exec":
                result = core.tools.code_exec.main(t["parameters"].get("code"))
                r = requests.post(
                    core.load_config.api()+core.load_config.key(),
                    data = json.dumps({"text": {"output": json.dumps(result}, "t": 1, "history": history})
                )
                res = json.loads(r.text)
                print(r.text)
                t = res["response"]
                history = json.dumps(res["history"])
            else:
                r = requests.post(
                    core.load_config.api()+core.load_config.key(),
                    data = json.dumps({"text": "Unknown tool.", "t": 1, "history": history})
                )
                res = json.loads(r.text)
                t = res["response"]
                history = json.dumps(res["history"])
        return t

