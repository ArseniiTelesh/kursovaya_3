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
        str_date = operation.get('date')
        date = datetime.datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
        return f'{date:%d.%m.%Y}'


def description_text(executed_list):
    for operation in executed_list:
        description = operation.get('description')
        return description


def card_number_of_sender(executed_list):
    for operation in executed_list:
        sender = operation.get('from')
        if sender is None:
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


def card_number_of_recipient(executed_list):
    for operation in executed_list:
        recipient = operation.get('to')
        recipient_list = recipient.split()

        if recipient_list[0] == 'Счет':
            numbers_of_account = '**' + recipient_list[1][16:]
            expected_answer = recipient_list[0] + ' ' + numbers_of_account
            return expected_answer

        elif recipient_list[0] == 'Visa':
            numbers_of_account = recipient_list[2][:4] + ' ' + recipient_list[2][4:6] + "** **** " + recipient_list[2][12:]
            expected_answer = ' '.join(recipient_list[:2]) + ' ' + numbers_of_account
            return expected_answer

        elif recipient_list[0] == 'Maestro' or 'MasterCard' or 'МИР':
            numbers_of_account = recipient_list[1][:4] + ' ' + recipient_list[1][4:6] + "** **** " + recipient_list[1][12:]
            expected_answer = recipient_list[0] + ' ' + numbers_of_account
            return expected_answer


def amount_and_currency(executed_list):
    for operation in executed_list:
        operationAmount = operation.get('operationAmount')

        amount = operationAmount.get('amount')
        currency = operationAmount.get('currency')
        a = currency.get('name')
        return ' '.join((amount, a))

