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
    for operation in executed_list:
        strdate = operation.get('date')
        date = datetime.datetime.strptime(strdate, '%Y-%m-%dT%H:%M:%S.%f')
        return f'{date:%d.%m.%Y}'


def description_text(executed_list):
    for operation in executed_list:
        description = operation.get('description')
        return description


def card_number_of_sender(executed_list):
    for operation in executed_list:
        sender = operation.get('from')
        if sender == None:
            continue
        sender_list = sender.split()
        if sender_list[0] == 'Счет':
            numbers_of_account = '**' + sender_list[1][16:]
            expected_answer = sender_list[0] + ' ' + numbers_of_account
            return expected_answer
        elif sender_list[0] == 'Visa':
            numbers_of_account = sender_list[2][:4] + ' ' + sender_list[2][4:6] + "** **** " + sender_list[2][12:]
            expected_answer = ' '.join(sender_list[:2]) + ' ' + numbers_of_account
            return expected_answer
        elif sender_list[0] == 'Maestro' or 'MasterCard' or 'МИР':
            numbers_of_account = sender_list[1][:4] + ' ' + sender_list[1][4:6] + "** **** " + sender_list[1][12:]
            expected_answer = sender_list[0] + ' ' + numbers_of_account
            return expected_answer
