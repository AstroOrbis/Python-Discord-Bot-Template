import json, os, sys

def loadConfig():
    if not os.path.isfile("config.json"):
        sys.exit("'config.json' not found! Please add it and try again.")
    else:
        with open("config.json") as file:
            config = json.load(file)

def dump_blacklist_json_data(file_data):
    with open("blacklist.json", "w") as file:
        file.seek(0)
        json.dump(file_data, file, indent=4)

def add_user_to_blacklist(user_id: int):
    with open("blacklist.json", "r+") as file:
        file_data = json.load(file)
        file_data["ids"].append(user_id)
    dump_blacklist_json_data(file_data)

def remove_user_from_blacklist(user_id: int):
    with open("blacklist.json", "r") as file:
        file_data = json.load(file)
        file_data["ids"].remove(user_id)
    dump_blacklist_json_data(file_data)