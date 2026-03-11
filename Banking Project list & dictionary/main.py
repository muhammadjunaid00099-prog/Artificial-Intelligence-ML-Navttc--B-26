import bankcore
import accounts


def main():

    print("Welcome to ABC Bank")

    current_user = ""

    while True:

        print("\n1. Login")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            cid = input("Enter customer id: ")
            password = input("Enter password: ")

            if bankcore.login(cid, password):
                current_user = cid

        elif choice == "2":
            name = input("Enter name: ")
            password = input("Enter password: ")

            cid = bankcore.create_account(name, password)
            accounts.balance_record[cid] = 0

        elif choice == "3":
            amount = float(input("Enter amount: "))
            accounts.deposit(current_user, amount)

        elif choice == "4":
            amount = float(input("Enter amount: "))
            accounts.withdraw(current_user, amount)

        elif choice == "5":
            accounts.check_balance(current_user)

        elif choice == "6":
            break

        else:
            print("Invalid choice")


main()