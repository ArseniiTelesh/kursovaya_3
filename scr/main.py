from scr.funcs import json_read, execution_list, sorted_time, description_text, \
    card_number_of_sender, card_number_of_recipient, amount_and_currency


def main():
    data = execution_list(json_read())
    for i in range(5):
        element = [data.pop()]

        if card_number_of_sender(element) is not None:
            print(f'''{sorted_time(element)} {description_text(element)}
{card_number_of_sender(element)} -> {card_number_of_recipient(element)}
{amount_and_currency(element)}
''')
        else:
            print(f'''{sorted_time(element)} {description_text(element)}
{card_number_of_recipient(element)}
{amount_and_currency(element)}
''')


main()
