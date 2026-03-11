branch_id = 2057
customer_id = None

Users_Info = {
    "2057-1": {"name": "Ali", "password": "12345"},
    "2057-2": {"name": "Saad", "password": "1234"},
    "2057-3": {"name": "Usman", "password": "123456"}
}

user_number = 4

def create_account(name, password):
    global customer_id
    global user_number

    customer_id = str(branch_id) + "-" + str(user_number)

    Users_Info[customer_id] = {
        "name": name,
        "password": str(password)
    }

    user_number += 1

    print("Account created successfully")
    print("Your Customer ID:", customer_id)

    return customer_id


def login(cid, password):

    if cid in Users_Info and Users_Info[cid]["password"] == str(password):
        print("Login Successful")
        return True
    else:
        print("Invalid login")
        return False