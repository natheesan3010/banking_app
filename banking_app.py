# Mini Banking Application using Procedural Programming


accounts = {}
next_account_number = 1001
  # Auto-generated account number

# Create Account
def create_account():
    global next_account_number
    
    name = input("Enter the user Name : ")
    password = input("Enter the password: ")
    name = input("Account Holder Name : ")
    nic = input("Enter your N.I.C_ Number : ")

    try:
        balance = float(input("Initial Deposit Amount: "))
        if balance < 0:
            print("Initial balance cannot be negative.")
        
    except ValueError:
             print("Invalid amount entered.")
            
    
    acc_no = next_account_number
    next_account_number += 1
    accounts[acc_no] = {
            'name': name,
            'balance': balance,
            'transaction': [f"Initial deposit: {balance}"]
        }
    
    print("Account created successfully! Account Number:",acc_no)

        #save acccount details in file
    with open("account.txt", "w") as file:
        file.write(f"{acc_no},{name},{nic}\n")

# Deposit Money
def deposit_money ():
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
        accounts[acc_no]['transaction'].append(f"Deposited: {amount}")
        print("Deposit successful.")
    except ValueError:
        print("Invalid input.")

    #save deposit details in file
    with open("deposit.txt", "a") as file:
        file.write(f"{acc_no},{amount}\n")


# Withdraw Money
def withdraw_money():
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
            print("invalid amount")
            return
        accounts[acc_no]['balance'] -= amount
        accounts[acc_no]['transaction'].append(f"Withdrawal: {amount}")
        print("Withdrawal successful.")
    except ValueError:
        print("Invalid input.")

    #save withdrawal details in file
    with open("withdrawal.txt", "a") as file:
        file.write(f"{acc_no},{amount}\n")   


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
            for n in accounts[acc_no]['transaction']:
                print(f"- {n}")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid account number.")
   

# Menu-driven interface
def admin_menu():
    while True:
        print("\n-----ADMIN MENU-----")
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

def user_menu ():
    while True:
        print("\n-----USER MENU-----")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            deposit_money()
        elif choice == '2':
            withdraw_money()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            transaction_history()
        elif choice == '5':
            print("Thank you for using the Mini Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")


def bank_app():
    while True:
        print("\n-----MINI BANKING APP MENU-----")
        print("1. ADMIN MENU")
        print("2. USER MENU")
        print("3. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            admin_menu()
        elif choice == '2':
            user_menu()
        elif choice == '3':
            print("Thank you for using the Mini Banking System.")
            break
        else:
            print("Invalid choice. Please try again.")

bank_app()