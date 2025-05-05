# Mini Banking Application using Procedural Programming

# user details
def user():
    #username = "admin"
    #password = "1234"

    # asking  information  user
    name = input("Enter the user Name : ")
    password = input("Enter the password: ")

    # user name and password checking
    if True:
        print("successful login!")
    else:
        print("check your user name and password then try again.")

accounts = {}
next_account_number = 1001  # Auto-generated account number

# Create Account
def create_account():
    global next_account_number
    user()
    name = input("Account Holder Name: ")
    try:
        balance = float(input("Initial Deposit Amount: "))
        if balance < 0:
            print("Initial balance cannot be negative.")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    acc_no = next_account_number
    next_account_number += 1
    accounts[acc_no] = {
        'name': name,
        'balance': balance,
        'transactions': [f"Initial deposit: {balance}"]
    }
    print(f"Account created successfully! Account Number: {acc_no}")

    #save acccount details in file
    with open("account.txt", "w") as file:
        file.write(f"{acc_no},{name}\n")


# Deposit Money
def deposit_money ():
    user()
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no not in accounts:
            print("Account not found.")
            return
        amount = float(input("Deposit Amount: "))
        if amount <= 0:
            print("Amount should be positive.")
            return
        accounts[acc_no]['balance'] += amount
        accounts[acc_no]['transactions'].append(f"Deposited: {amount}")
        print("Deposit successful.")
    except ValueError:
        print("Invalid input.")

# Withdraw Money
def withdraw_money():
    user()
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no not in accounts:
            print("Account not found.")
            return
        amount = float(input("Withdrawal Amount: "))
        if amount <= 0:
            print("Amount must positive.")
            return
        if amount > accounts[acc_no]['balance']:
            print(".")
            return
        accounts[acc_no]['balance'] -= amount
        accounts[acc_no]['transactions'].append(f"Withdrawn: {amount}")
        print("Withdrawal successful.")
    except ValueError:
        print("Invalid input.")

# Check Balance
def check_balance():
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            print(f"Current Balance: {accounts[acc_no]['balance']}")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid account number.")

# Transaction History
def transaction_history():
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            print("Transaction History:")
            for txn in accounts[acc_no]['transactions']:
                print(f"- {txn}")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid account number.")

# Menu-driven interface
def menu():
    while True:
        print("\n----- Mini Banking System -----")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

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
            print("Thank you for using the Mini Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")

# Program starts here
menu()


