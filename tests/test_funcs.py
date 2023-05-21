from scr.funcs import json_read, execution_list, sorted_time, description_text, \
    card_number_of_sender, card_number_of_recipient, amount_and_currency
from scr.main import main

operations = json_read()


def test_json_read():
    assert json_read() == operations


def test_execution_list():
    assert execution_list([{'state': 'EXECUTED'}, {'state': 'CANCELED'}]) == [{'state': 'EXECUTED'}]


def test_sorted_time():
    assert sorted_time([{'date': '2019-08-26T10:50:58.294041'}, {'date': '2018-06-30T02:08:58.425572'}]) == '26.08.2019'


def test_description_text():
    assert description_text([{"description": "Перевод"}, {"fjgerfu": 32423}]) == "Перевод"
    assert description_text([{"defption": "Перевод"}]) != "Перевод"


def test_card_number_of_sender():
    assert card_number_of_sender([{"from": "Счет 54883981902864782073"}]) == 'Счет **2073'
    assert card_number_of_sender([{"from": "MasterCard 1435442169918409"}]) == 'MasterCard 1435 44** **** 8409'
    assert card_number_of_sender([{"from": "Visa Classic 6216537926639975"}]) == 'Visa Classic 6216 53** **** 9975'
    assert card_number_of_sender([{"description": "Открытие вклада"}]) is None


def test_card_number_of_recipient():
    assert card_number_of_recipient([{"to": "Счет 12189246980267075758"}]) == 'Счет **5758'
    assert card_number_of_recipient([{"to": "Maestro 6890749237669619"}]) == 'Maestro 6890 74** **** 9619'
    assert card_number_of_recipient([{"to": "Visa Gold 8702717057933248"}]) == 'Visa Gold 8702 71** **** 3248'
    assert card_number_of_recipient([{"to": "МИР 2052809263194182"}]) == 'МИР 2052 80** **** 4182'


def test_amount_and_currency():
    assert amount_and_currency([{"operationAmount": {
        "amount": "37044.95", "currency": {"name": "руб.", "code": "RUB"}}}]) == '37044.95 руб.'


def test_main():
    assert main() is None
