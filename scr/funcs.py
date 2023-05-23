import json
import datetime


def json_read():
    """
    Возвращает json-файл
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        text = json.load(file)

    return text


def execution_list(text):
    """
    Принимает json-файл и возвращает отсортированный список
    только с выполненными операциями, также сортирует по времени
    """
    executed_list = []
    for operation in text:
        if operation.get("state") == "EXECUTED":
            executed_list.append(operation)

    executed_list = sorted(
        executed_list, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=False
    )


    return executed_list


def sorted_time(executed_list):
    """
    Принимает остортированный список операций и
    возвращает формат времени одной операции в соответствии с заданием
    """
    for operation in executed_list:
        str_date = operation.get('date')
        date = datetime.datetime.strptime(str_date, '%Y-%m-%dT%H:%M:%S.%f')
        return f'{date:%d.%m.%Y}'


def description_text(executed_list):
    """
        Принимает остортированный список операций и
        возвращает описание одной операции
        """
    for operation in executed_list:
        description = operation.get('description')
        return description


def card_number_of_sender(executed_list):
    """
        Принимает остортированный список операций и
        возвращает номер карты отправителя одной операции в соответствии с заданием
        """
    for operation in executed_list:
        sender = operation.get('from')
        if sender is None:
            break
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
    """
    Принимает остортированный список операций и
    возвращает номер карты получателя одной операции в соответствии с заданием
    """
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
    """
    Принимает остортированный список операций и
    возвращает сумму и валюту одной операции в соответствии с заданием
    """
    for operation in executed_list:
        operation_amount = operation.get('operationAmount')

        amount = operation_amount.get('amount')
        currency = operation_amount.get('currency')
        name_of_currency = currency.get('name')
        return ' '.join((amount, name_of_currency))
