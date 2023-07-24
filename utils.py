import json
import datetime


def get_transactions(path):
    with open(path, "rt", encoding="utf-8") as file_json:
        transactions = json.load(file_json)
        return transactions


def get_filtered_transactions(transactions):
    transactions_list = []
    for transaction in transactions:
        for key in transaction.keys():
            if key == 'state':
                if transaction['state'] == 'EXECUTED':
                    transactions_list.append(transaction)
    return transactions_list


def get_sorted_transactions(transactions):
    transactions = sorted(transactions, key=lambda x: x['date'])
    return transactions[-5:]


def get_formatted_transactions(transactions):
    list_transactions = []
    for i in range(len(transactions)):
        old_transactions = transactions[i]['date']
        date_transactions = datetime.datetime.strptime(old_transactions, "%Y-%m-%dT%H:%M:%S.%f")
        date_transactions = date_transactions.strftime("%d.%m.%Y")
        list_transactions.append(date_transactions)

    return f"{list_transactions[0]} {transactions[0]['description']} \n{transactions[0].get('from')} \
    -> {transactions[0]['to'][:5]}**{transactions[0]['to'][21:]}\n{transactions[0]['operationAmount']['amount']} руб.\n\n" \
           f"{list_transactions[1]} {transactions[1]['description']} \n{transactions[1].get('from')[:5]}**\
{transactions[1].get('from')[21:]} \
    -> {transactions[1]['to'][:5]}**{transactions[1]['to'][21:]}\n{transactions[1]['operationAmount']['amount']} руб.\n\n" \
           f"{list_transactions[2]} {transactions[2]['description']} \n{transactions[2].get('from')[:12]} \
{transactions[2].get('from')[13:15]}** **** {transactions[2].get('from')[20:]}\
    -> {transactions[2]['to'][:5]}**{transactions[2]['to'][21:]}\n{transactions[2]['operationAmount']['amount']} руб.\n\n" \
           f"{list_transactions[3]} {transactions[3]['description']} \n{transactions[3].get('from')[:17]} \
{transactions[3].get('from')[18:20]}** **** {transactions[3].get('from')[25:]}\
    -> {transactions[3]['to'][:5]}**{transactions[3]['to'][21:]}\n{transactions[3]['operationAmount']['amount']} руб.\n\n" \
           f"{list_transactions[4]} {transactions[4]['description']} \n{transactions[4].get('from')} \
    -> {transactions[4]['to'][:5]}**{transactions[4]['to'][21:]}\n{transactions[4]['operationAmount']['amount']} руб."
