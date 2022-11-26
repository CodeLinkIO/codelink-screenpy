import json


def read_file(path):
    with open(path) as file:
        return json.load(file)
