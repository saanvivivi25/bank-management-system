import random
min_bal = 500.0
rate = 0.0725
accounts = {}

def generate_acc_no():
    while True:
        acc_no = str(random.randint(1,1000))
        if acc_no not in accounts:
            return acc_no
        
def create_account():
    acc_no = generate_acc_no()
    print(f"Your Account Number is: {acc_no}")
    name = input("Enter Name: ")
    type_choice = input("Choose Type (1. Savings 2. Current): ")
    if type_choice == '2':
        print("Current Account feature is Work Under Progress")
        return
    acc_type = "Savings"
    amount = float(input("Enter Initial Deposit: "))
    if amount < min_bal:
        return print(f"Failed: Minimum balance is {min_bal}")
    accounts[acc_no] = {"name": name, "bal": amount, "type": acc_type}
    print("Account Created Successfully!")



def deposit():
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        return print("Account Not Found")
    amount = float(input("Enter Amount: "))
    accounts[acc_no]["bal"] += amount
    print(f"New Balance: {accounts[acc_no]['bal']}")

def withdraw():
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        return print("Account Not Found")
    acc = accounts[acc_no]
    amount = float(input("Enter Amount: "))
    if acc["bal"] - amount < min_bal:
        print(f"Maintain {min_bal}")
    else:
        acc["bal"] -= amount
        print(f"New Balance: {acc['bal']}")

def apply_interest():
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        return print("Account Not Found")
    acc = accounts[acc_no]
    if acc["type"] == "Savings":
        interest = acc["bal"] * rate
        acc["bal"] += interest
        print(f"Interest of {rate * 100}% added!")
        print(f"New Balance: {acc['bal']:.2f}")
    else:
        print("Interest only applies to Savings accounts.")

def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        acc = accounts[acc_no]
        print(f"Holder: {acc['name']} | Type: {acc['type']} | Balance: {acc['bal']}")
    else:
        print("Account Not Found")

def display_all():
    print("\n All Accounts ")
    for id, info in accounts.items():
        print(f"ID: {id} | {info['name']} | {info['type']} | Bal: {info['bal']}")

while True:
    print("\n Bank Management System ")
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Display All Accounts\n6. Apply Interest (Savings)\n7. Exit")
    choice = input("Enter your choice: ")
    if choice == '1': 
        create_account()
    elif choice == '2': 
        deposit()
    elif choice == '3': 
        withdraw()
    elif choice == '4': 
        check_balance()
    elif choice == '5': 
        display_all()
    elif choice == '6':
        apply_interest()
    elif choice == '7':
        print("Thank you")
        break
    else:
        print("Invalid Choice")	