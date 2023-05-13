import os
import json


def json_read():
    path = os.path.join('../operations.json')
    with open(path, 'r', encoding='utf-8') as file:
        text = json.load(file)

    return text


def execution_list(text):
    executed_list = []
    for operation in text:
        if operation.get("state") == "EXECUTED":
            executed_list.append(operation)

    return executed_list

