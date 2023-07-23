from utils import get_transactions, get_filtered_transactions, get_sorted_transactions, get_formatted_transactions


def main():
    print('Курсовая работа №3')
    transactions = get_transactions('operations.json')
    transactions = get_filtered_transactions(transactions)
    transactions = get_sorted_transactions(transactions)
    transactions = get_formatted_transactions(transactions)
    print(transactions)



if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
