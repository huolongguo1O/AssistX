import json
api_list = json.load(open("api_list.json"))
def is_valid(key):
    for api in api_list:
        if api["key"] == key:
            return True
    return False

def add_key(key):
    if is_valid(key):
        return False
    api_list.append({"key": key, "count": 0})
    json.dump(api_list, open("api_list.json", "w"))
    return True