import os
import json


def json_read():
    path = os.path.join('../operations.json')
    with open(path, 'r', encoding='utf-8') as file:
        text = json.load(file)

    return text


