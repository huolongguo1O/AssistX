api_list = json.load(open("api_list.json"))
def is_valid():
    for api in api_list:
        if api