import requests
import json
import load_config
history = "None"
def chat(msg):
    '''
class query(BaseModel):
    text: str
    _type: int # 0 for chat and 1 for observation
    history: str
    '''
    requests.get(
        load_config.api()+load_config.key()
        
    )