import requests
import json
import load_config
history = "None"
def chat(msg):
    requests.get(load_config.api()+load_config)