import random

all_accounts = {}

def create_acc():
    fname = input("Enter your first name: ")
    mname = input("Enter your middle name: ")
    lname = input("Enter your last name: ")
    fullname = fname + " " + mname + " " + lname

    account_num = str(random.randint(10000000, 99999999))
    print("Your account number is: ", account_num)

    while True:
        pin = input(f"Enter a 4-digit PIN for account number {account_num}: ")
        if not pin.isdigit() or len(pin) != 4:
            print("PIN must be exactly 4 digits and only contain numbers.")
        else:
            break

    account_data = {
        "Full Name": fullname,
        "PIN": pin,
        "Current Balance": 0
    }
    all_accounts[account_num] = account_data

    print("\nACCOUNT CREATED SUCCESSFULLY")
    print("THE DETAILS ARE AS FOLLOWING:")
    print(f"Account Number: {account_num}")
    for key, value in account_data.items():
        print(f"{key}: {value}")

def deposit_money():
    daccno = input("Enter your account number: ")
    if daccno not in all_accounts:
        print("ACCOUNT NUMBER NOT FOUND.")
        return
    else:
        print("ACCOUNT NUMBER VERIFIED")

    dpin = input("Enter your PIN: ")
    if dpin != all_accounts[daccno]["PIN"]:
        print("Incorrect PIN.")
        return

    amount = input("Enter amount to deposit: ")
    if not amount.isdigit():
        print("Invalid amount. Please enter numbers only.")
        return

    amount = int(amount)
    all_accounts[daccno]["Current Balance"] += amount
    print(f"₹{amount} deposited successfully.")
    print(f"Updated Balance: ₹{all_accounts[daccno]['Current Balance']}")

def withdraw_money():
    waccno = input("Enter your account number: ")
    if waccno not in all_accounts:
        print("ACCOUNT NUMBER NOT FOUND.")
        return
    else:
        print("ACCOUNT NUMBER VERIFIED")

    wpin = input("Enter your PIN: ")
    if wpin != all_accounts[waccno]["PIN"]:
        print("Incorrect PIN.")
        return

    amount = input("Enter amount to withdraw: ")
    if not amount.isdigit():
        print("Invalid amount. Please enter numbers only.")
        return

    amount = int(amount)
    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if all_accounts[waccno]["Current Balance"] < amount:
        print("You do not have enough balance.")
        return

    all_accounts[waccno]["Current Balance"] -= amount
    print(f"₹{amount} withdrawn successfully.")
    print(f"Updated Balance: ₹{all_accounts[waccno]['Current Balance']}")

def check_balance():
    baccno = input("Enter your account number: ")
    if baccno not in all_accounts:
        print("ACCOUNT NUMBER NOT FOUND.")
        return
    else:
        print("ACCOUNT NUMBER VERIFIED")

    bpin = input("Enter your PIN: ")
    if bpin != all_accounts[baccno]["PIN"]:
        print("Incorrect PIN.")
        return

    balance = all_accounts[baccno]["Current Balance"]
    print(f"Your current balance is: ₹{balance}")

# Main menu loop
while True:
    print("\nMENU")
    print("1. Create new account")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Check balance")
    print("5. Exit")
    try:
        menu = int(input("Enter your choice: "))
        match menu:
            case 1:
                create_acc()
            case 2:
                deposit_money()
            case 3:
                withdraw_money()
            case 4:
                check_balance()
            case 5:
                print("Thank you for using our banking system!")
                break
            case _:
                print("Invalid option. Please choose from 1 to 5.")
    except ValueError:
        print("Please enter a valid number.")
