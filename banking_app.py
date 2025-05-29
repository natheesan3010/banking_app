import random
from datetime import datetime

accounts = {}
ID = random.randint(1000, 9999)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def show_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Current Date: {current_date}")

def get_existing_usernames():
    usernames = set()
    try:
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) >= 1:
                    usernames.add(data[0])
    except FileNotFoundError:
        pass
    return usernames

def load_accounts():
    try:
        with open("users.txt", "r") as user_file:
            for line in user_file:
                username, password, user_id, acc_no = line.strip().split(",")
                acc_no = int(acc_no)
                accounts[acc_no] = {'transaction': []}

        with open("account.txt", "r") as acc_file:
            for line in acc_file:
                acc_no, user_id, name, nic, address, contact = line.strip().split(",")
                acc_no = int(acc_no)
                if acc_no in accounts:
                    accounts[acc_no]['name'] = name
                    accounts[acc_no]['balance'] = 0
    except FileNotFoundError:
        pass

def save_balance():
    with open("balances.txt", "w") as file:
        for acc_no, data in accounts.items():
            file.write(f"{acc_no},{data['balance']}\n")

def save_transaction(acc_no, transaction):
    with open("transactions.txt", "a") as file:
        file.write(f"{acc_no},{transaction}\n")

def get_account():
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            return acc_no
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid account number.")
    return None

def admin_login():
    print("---- Admin Login ----")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print(f"Welcome to our bank {username} (Admin)")
        return True
    else:
        print("Invalid admin credentials.")
        return False

def login_user():
    username = input("Enter username : ")
    password = input("Enter password : ")
    try:
        with open("users.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == username and data[1] == password:
                    print(f"\nLogin successful! Welcome {username}")
                    print(f" Account No: {data[3]}\n User ID: {data[2]}\n")
                    return int(data[3])
        print("Login failed! Invalid username or password.")
    except FileNotFoundError:
        print("User file not found.")
    return None

def create_account():
    global ID
    existing_usernames = get_existing_usernames()
    while True:
        username = input("Enter the user Name : ")
        if username in existing_usernames:
            print("Username already taken. Try another.")
        else:
            break

    password = input("Enter the password : ")
    name = input("Account Holder Name : ").title()
    if not all(x.isalpha() or x.isspace() for x in name):
        print("Invalid name.")
        return

    nic = input("Enter your N.I.C_ Number : ")
    if len(nic) != 12 or not nic.isdigit():
        print("Invalid NIC Number.")
        return 

    address = input("Enter your address : ")
    contact = input("Enter your Contact Number : ")
    balance = float(input("Enter The Initial Balance : "))

    user_id = f"U_{ID}"
    acc_no = ID
    ID += 1

    accounts[acc_no] = {
        'name': name,
        'balance': balance,
        'transaction': [f"Account created with initial balance: {balance}"]
    }

    with open("users.txt", "a") as f:
        f.write(f"{username},{password},{user_id},{acc_no}\n")

    with open("account.txt", "a") as file:
        file.write(f"{acc_no},{user_id},{name},{nic},{address},{contact}\n")

    print(f"Welcome {username} (Customer)")
    print(f"Account Number: {acc_no}, User ID: {user_id}")

def deposit_money():
    acc_no = get_account()
    if acc_no is None:
        return
    try:
        amount = float(input("Deposit Amount: "))
        if amount <= 0:
            print("Amount should be positive.")
            return
        accounts[acc_no]['balance'] += amount
        transaction = f"Deposited: {amount}"
        accounts[acc_no]['transaction'].append(transaction)
        save_transaction(acc_no, transaction)
        print("Deposit successful.")
    except ValueError:
        print("Invalid input.")

def withdraw_money():
    acc_no = get_account()
    if acc_no is None:
        return
    try:
        amount = float(input("Withdrawal Amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > accounts[acc_no]['balance']:
            print("Insufficient balance.")
            return
        accounts[acc_no]['balance'] -= amount
        transaction = f"Withdrawal: {amount}"
        accounts[acc_no]['transaction'].append(transaction)
        save_transaction(acc_no, transaction)
        print("Withdrawal successful.")
    except ValueError:
        print("Invalid input.")

def check_balance():
    acc_no = get_account()
    if acc_no is None:
        return
    balance = accounts[acc_no]['balance']
    print(f"Current balance for account {acc_no}: Rs. {balance}")


def transfer_funds():
    print("----- Fund Transfer -----")
    from_acc = get_account()
    if from_acc is None:
        return
    to_acc = int(input("Enter recipient account number: "))
    if to_acc not in accounts:
        print("Recipient account not found.")
        return
    try:
        amount = float(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if accounts[from_acc]['balance'] < amount:
            print("Insufficient balance.")
            return
        accounts[from_acc]['balance'] -= amount
        accounts[to_acc]['balance'] += amount
        accounts[from_acc]['transaction'].append(f"Transferred {amount} to {to_acc}")
        accounts[to_acc]['transaction'].append(f"Received {amount} from {from_acc}")
        save_transaction(from_acc, f"Transferred: {amount} to {to_acc}")
        save_transaction(to_acc, f"Received: {amount} from {from_acc}")
        print("Transfer successful.")
    except ValueError:
        print("Invalid amount.")

def transaction_history():
    acc_no = get_account()
    if acc_no is not None:
        print("Transaction History:")
        for t in accounts[acc_no]['transaction']:
            print(f"- {t}")

def transaction_type_summary():
    acc_no = get_account()
    if acc_no is None:
        return
    deposit_count = 0
    withdraw_count = 0
    try:
        with open("transactions.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",", 1)
                if len(parts) == 2:
                    trans_acc_no, description = parts
                    if int(trans_acc_no) == acc_no:
                        if description.startswith("Deposited"):
                            deposit_count += 1
                        elif description.startswith("Withdrawal"):
                            withdraw_count += 1
        print(f"Deposits: {deposit_count}, Withdrawals: {withdraw_count}")
    except FileNotFoundError:
        print("Transaction file not found.")

def count_transactions():
    acc_no = get_account()
    if acc_no is None:
        return
    try:
        count = sum(1 for line in open("transactions.txt") if line.startswith(str(acc_no)))
        print(f"Total transactions for account {acc_no}: {count}")
    except FileNotFoundError:
        print("Transaction file not found.")

def count_total_customers():
    try:
        with open("users.txt", "r") as file:
            customers = sum(1 for line in file)
        print(f"Total number of customers: {customers}")
    except FileNotFoundError:
        print("User file not found.")

def update_account():
    acc_no = get_account()
    if acc_no is None:
        return
    name = input("New name: ").title()
    address = input("New address: ")
    contact = input("New contact number: ")
    try:
        lines = []
        with open("account.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if int(parts[0]) == acc_no:
                    parts[2] = name
                    parts[4] = address
                    parts[5] = contact
                lines.append(",".join(parts))
        with open("account.txt", "w") as file:
            for line in lines:
                file.write(line + "\n")
        print("Account updated successfully.")
    except FileNotFoundError:
        print("Account file not found.")

def delete_account():
    acc_no = get_account()
    if acc_no is None:
        return
    try:
        with open("users.txt", "r") as file:
            lines = [line for line in file if str(acc_no) not in line]
        with open("users.txt", "w") as file:
            file.writelines(lines)

        with open("account.txt", "r") as file:
            lines = [line for line in file if str(acc_no) not in line]
        with open("account.txt", "w") as file:
            file.writelines(lines)

        if acc_no in accounts:
            del accounts[acc_no]

        print("Account deleted successfully.")
    except FileNotFoundError:
        print("File not found.")

def admin_menu():
    while True:
        print("\n-----ADMIN MENU-----")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Current Date")
        print("7. Transaction Type Summary")
        print("8. Fund Transfer")
        print("9. Update Account")
        print("10. Delete Account")
        print("11. Count Transactions")
        print("12. Count Total Customers")
        print("13. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit_money()
        elif choice == '3':
            withdraw_money()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            transaction_history()
        elif choice == '6':
            show_current_date()
        elif choice == '7':
            transaction_type_summary()
        elif choice == '8':
            transfer_funds()
        elif choice == '9':
            update_account()
        elif choice == '10':
            delete_account()
        elif choice == '11':
            count_transactions()
        elif choice == '12':
            count_total_customers()
        elif choice == '13':
            save_balance()
            break
        else:
            print("Invalid choice.")

def user_menu():
    acc_no = login_user()
    if acc_no is None:
        return
    while True:
        print("\n-----USER MENU-----")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Fund Transfer")
        print("6. Current Date")
        print("7. Transaction Type Summary")
        print("8. Count Transactions")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            deposit_money()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            transaction_history()
        elif choice == '5':
            transfer_funds()
        elif choice == '6':
            show_current_date()
        elif choice == '7':
            transaction_type_summary()
        elif choice == '8':
            count_transactions()
        elif choice == '9':
            save_balance()
            break
        else:
            print("Invalid choice.")

def bank_app():
    load_accounts()
    while True:
        print("\n-----MINI BANKING APP MENU-----")
        print("1. ADMIN MENU")
        print("2. USER MENU")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            if admin_login():
                admin_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            save_balance()
            break
        else:
            print("Invalid choice.")

bank_app()
