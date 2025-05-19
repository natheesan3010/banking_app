
# Mini Banking Application using Procedural Programming
import random
from datetime import datetime

accounts = {}
ID = random.randint(1000, 9999)

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

# Admin 
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def show_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    print(f"Current Date: {current_date}")

# Load Accounts from File
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


# Save balance in balances.txt file
def save_balance():
    with open("balances.txt", "a") as file:
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

# Admin login function
def admin_login():
    print("---- Admin Login ----")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        print(f"welcome to our bank {username} (Admin)")
        print("Admin login successful!")
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

    # Username availability check
    existing_usernames = get_existing_usernames()
    while True:
        username = input("Enter the user Name : ")
        if username in existing_usernames:
            print("Username already taken. Try another.")
        else:
            break

    password = input("Enter the password : ")
    name = input("Account Holder Name : ")

    name = name.title()  # Title case

    if not all(x.isalpha() or x.isspace() for x in name):
        print("Invalid name. Only letters and spaces are allowed.")
        return

    nic = input("Enter your N.I.C_ Number : ")
    if len(nic) != 12 or not nic.isdigit():
        print("Invalid NIC Number. It must be 12 digits.")
        return 

    address = input("Enter your address : ")
    contact = int(input("Enter your Contact Number : "))

    user_id = f"U_{ID}"
    acc_no = ID
    ID += 1

    balance = int(input("Enter The Initial Balance : "))
    accounts[acc_no] = {
        'name': name,
        'balance': balance,
        'transaction': [f"Account created with initial balance: {balance}"]
    }

    with open("users.txt", "a") as f:
        f.write(f"{username},{password},{user_id},{acc_no}\n")
    print(f"Welcome to our bank {username} (customer)\n")
    print(f" Account created successfully! \n Account Number: {acc_no} \n user ID :{user_id}")

    with open("account.txt", "a") as file:
        file.write(f"{acc_no},{user_id},{name},{nic},{address},{contact}\n")


    with open("users.txt", "a") as f:
        f.write(f"{user_id},{username},{password},{acc_no}\n")
    print(f"Welcome to our bank {username} (customer)\n")#E2
    print(f" Account created successfully! \n Account Number: {acc_no} \n user ID :{user_id}")

    with open("account.txt", "a") as file:
        file.write(f"{acc_no},{user_id},{name},{nic},{address},{contact}\n")



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


def transaction_type_summary():
    acc_no = get_account()
    if acc_no is None:
        return

    try:
        deposit_count = 0
        withdraw_count = 0
        found = False

        with open("transactions.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",", 1)
                if len(parts) == 2:
                    trans_acc_no, description = parts
                    if int(trans_acc_no) == acc_no:
                        found = True
                        if description.startswith("Deposited"):
                            deposit_count += 1
                        elif description.startswith("Withdrawal"):
                            withdraw_count += 1

        if found:
            print(f"Deposits: {deposit_count}, Withdrawals: {withdraw_count}")
        else:
            print("No transactions found for this account.")
    except FileNotFoundError:
        print("Transaction file not found.")


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
    if acc_no is not None:
        print(f"Current Balance: {accounts[acc_no]['balance']}")

def transaction_history():
    acc_no = get_account()
    if acc_no is not None:
        print("Transaction History:")
        for n in accounts[acc_no]['transaction']:
            print(f"- {n}")

# Admin interface
def admin_menu():
    while True:
        print("\n-----ADMIN MENU-----")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Current Date")
        print("7. Transaction Type Sumary")
        print("8. Exit")

        choice = input(f"Enter your choice (1-6): \n ")

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
            save_balance()
            print("Thank you for using the Mini Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")

# User interface
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
        print("5. Current Date")
        print("6. Transaction Type Sumary")
        print("7. Exit")

        choice = input(f"Enter your choice (1-5): \n")

        if choice == '1':
            deposit_money()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            transaction_history()
        elif choice == '5':
            show_current_date()
        elif choice == '6':
            transaction_type_summary()
        elif choice == '7':
            save_balance()
            print("Thank you for using the Mini Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")

# App user interface
def bank_app():
    load_accounts()
    while True:
        print("\n-----MINI BANKING APP MENU-----")
        print("1. ADMIN MENU")
        print("2. USER MENU")
        print("3. Exit")

        choice = input(f"Enter your choice (1-3): \n")

        if choice == '1':
            if admin_login():
                admin_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            save_balance()
            print("Thank you for using the Mini Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start app
bank_app()

