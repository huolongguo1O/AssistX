api_list = json.load(open("api_list.json"))
def is_valid(key):
    for api in api_list:
        if api["key"] == key:
            return Treu
    