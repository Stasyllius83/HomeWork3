from utils import get_transactions, get_filtered_transactions, get_sorted_transactions, get_formatted_transactions


def test_get_transactions():
    assert isinstance(get_transactions(path='../operations.json'), list)


def test_get_filtered_transactions():
    assert len(get_filtered_transactions([{'state': 'EXECUTED'}, {'state': 'CANCELED'}])) == 1


def test_get_sorted_transactions():
    assert get_sorted_transactions([{'date': '2019-12-08T22:46:21.935582'}, {"date": "2019-05-11T18:51:29.313309"}, \
                                    {'date': '2019-12-07T06:17:14.634890'}, {'date': '2019-11-19T09:22:25.899614'}, \
                                    {'date': '2019-11-13T17:38:04.800051'}]) == \
                                    [{"date": "2019-05-11T18:51:29.313309"}, {'date': '2019-11-13T17:38:04.800051'}, \
                                    {'date': '2019-11-19T09:22:25.899614'}, {'date': '2019-12-07T06:17:14.634890'}, \
                                    {'date': '2019-12-08T22:46:21.935582'}]


def test_get_formatted_transactions():
    assert get_formatted_transactions([
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725",
            "operationAmount": {
                "amount": "21344.35",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада ",
            "to": "Счет 77613226829885488381"
        },
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        },
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
            "operationAmount": {
                "amount": "30153.72",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 7810846596785568",
            "to": "Счет 43241152692663622869"
        },
        {
            "id": 114832369,
            "state": "EXECUTED",
            "date": "2019-12-07T06:17:14.634890",
            "operationAmount": {
                "amount": "48150.39",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Classic 2842878893689012",
            "to": "Счет 35158586384610753655"
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {
                "amount": "41096.24",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907"
        }]
    ) == "05.11.2019 Открытие вклада \n""None -> Счет **8381\n""21344.35 руб.\n\n" \
         "13.11.2019 Перевод со счета на счет\n""Счет **9794 -> Счет **8125\n""62814.53 руб.\n\n" \
         "19.11.2019 Перевод организации\n""Maestro 7810 46** **** 5568 -> Счет **2869\n""30153.72 руб.\n\n" \
         "07.12.2019 Перевод организации\n""Visa Classic 2842 78** **** 9012 -> Счет **3655\n""48150.39 руб.\n\n" \
         "08.12.2019 Открытие вклада\n""None -> Счет **5907\n""41096.24 руб."
