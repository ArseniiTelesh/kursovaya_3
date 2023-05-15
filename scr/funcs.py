import json
import datetime


def json_read():
    with open('operations.json', 'r', encoding='utf-8') as file:
        text = json.load(file)

    return text


def execution_list(text):
    executed_list = []
    for operation in text:
        if operation.get("state") == "EXECUTED":
            executed_list.append(operation)

    return executed_list


def sorted_time(executed_list):
    for operations in executed_list:
        strdate = operations.get('date')
        date = datetime.datetime.strptime(strdate, '%Y-%m-%dT%H:%M:%S.%f')
        return f'{date:%d.%m.%Y}'


def description_text(executed_list):
    for operations in executed_list:
        description = operations.get('description')
        return description

