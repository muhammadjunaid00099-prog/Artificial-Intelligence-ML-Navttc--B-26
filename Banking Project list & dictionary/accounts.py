balance_record = {
    "2057-1": 5000,
    "2057-2": 3000,
    "2057-3": 7000
}

def check_balance(customer_id):

    balance = balance_record.get(customer_id, 0)
    print("Your balance is:", balance)


def deposit(customer_id, amount):

    balance = balance_record.get(customer_id, 0)
    balance += amount
    balance_record[customer_id] = balance

    print("Amount deposited successfully")


def withdraw(customer_id, amount):

    balance = balance_record.get(customer_id, 0)

    if amount <= balance:
        balance -= amount
        balance_record[customer_id] = balance
        print("Withdraw successful")
    else:
        print("Insufficient balance")