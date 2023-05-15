from scr.funcs import json_read, execution_list, sorted_time, description_text

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
