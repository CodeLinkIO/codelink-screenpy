import json
from functools import reduce


def read_file(path):
    with open(path) as file:
        return json.load(file)


def get_value_or_default(dictionary, keys, default=None):
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("."), dictionary)



