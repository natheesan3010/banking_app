import random
import os

accounts = {}
 # Auto-generated account number
acc_no = 1001 



# auto id
def create_id(id):
    return id + str(random.randint(1000, 9999))

# Register function
def create_account():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    user_id = create_id("u_id")
    customer_id = create_id("C_ID")

    #save acccount details in file
    with open("account.txt", "a") as file:
        file.write(f"{acc_no},{username},{password},{user_id},{customer_id}\n")

    print("Registered successfully!")
    print(f"Your User ID: {user_id}")
    print(f"Your Customer ID: {customer_id}")

    
    name = input("Account Holder Name: ")
    try:
        balance = float(input("Initial Deposit Amount: "))
        if balance < 0:
            print("Initial balance cannot be negative.")
            return
    except ValueError:
        print("Invalid amount entered.")
    
    #save in file
    with open("trancetion.txt", "a") as file:
        file.write(f"{acc_no},{user_id},{balance}\n")

    return

  
    acc_no += 1
    #global name,balance
    accounts[acc_no] = {
        "name": name,
        "balance": balance,
        trancetion: [f"Initial deposit: {balance}"]
    }
    print(f"Account created successfully! Account Number: {acc_no}")
    
    #save in file
    with open("balance.txt", "a") as file:
        file.write(f"{acc_no},{name},{customer_id},{balance}\n")


# Usermenu
def creat_menu():
    while True:
        print("===USERS ACCOUNT===")
        print("1. Register")
        #print("2. Login")
        print("2. Exit")
        choice = input("Enter your choice : ")

        if choice == '1':
           create_account()
        #elif choice == '2':
        #    login()
        elif choice == '2':
            print("Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

'''
#deposit fountion
def deposit ():
    while

#withdraw fountion
def withdraw ():
    while
'''
#balance fountion
def balance ():
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            print(f"Current Balance: {accounts[acc_no]['balance']}")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid account number.")

#trancetion fountion
def trancetion ():
    global balance
    try:
        acc_no = int(input("Enter Account Number: "))
        if acc_no in accounts:
            print("Trancetion History:")
            for i in accounts[acc_no]:
                print(f"- {i}")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid account number.")

    #save in file
    #with open("trancetion.txt", "r") as file:
        #file.write(f"{acc_no},{balance}\n")




#banking main menu
def main_menu():
    while True:
        print("=====BANK MAIN MENU=====")
        print("1. CREAT ACCOUNT")
        #print("2. DEPOSIT AMOUNT")
        #print("3. WITHDRAW AMOUNT")
        print("4. CHECK BALANCE")
        print("5. VIEW TRANSECTION HISTROY")
        print("6. EXIT")
        
        choice = input("Enter your choice (1 - 6): ")

        if choice == '1':
            creat_menu()
        #elif choice == '2':
            #deposit()
        #elif choice == '3':
           # withdraw() 
        elif choice == '4':
            balance()
        elif choice == '5':
            trancetion()
        elif choice == '6':
            print("Thank You For Banking Us! Have A Nice Day! ")
        else:
            print("Invalid choice! Try again!.")

main_menu()
