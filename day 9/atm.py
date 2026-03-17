"""Simple ATM simulator.

Features:
- Login with account number + PIN
- Check balance
- Deposit
- Withdraw
- View transaction history
- Change PIN
"""

from datetime import datetime

# Sample in-memory account database
# In a real app, this would be persisted to a file/db.
accounts = {
    "1001": {"pin": "1234", "balance": 1500.0, "transactions": []},
    "1002": {"pin": "0000", "balance": 750.0, "transactions": []},
}


def menu() -> None:
    print("\n----- ATM Menu -----")
    print("[C]heck balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[V]iew transactions")
    print("[P]in change")
    print("[E]xit")


def record_transaction(acc_num: str, desc: str, amount: float) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    accounts[acc_num]["transactions"].append({"time": now, "desc": desc, "amount": amount})


def check_balance(acc_num: str) -> None:
    balance = accounts[acc_num]["balance"]
    print(f"\nYour current balance is: ₹{balance:.2f}")


def deposit(acc_num: str) -> None:
    try:
        amt = float(input("Enter amount to deposit: ₹"))
        if amt <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    accounts[acc_num]["balance"] += amt
    record_transaction(acc_num, "Deposit", amt)
    print(f"Deposited ₹{amt:.2f}. New balance: ₹{accounts[acc_num]['balance']:.2f}")


def withdraw(acc_num: str) -> None:
    try:
        amt = float(input("Enter amount to withdraw: ₹"))
        if amt <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    if amt > accounts[acc_num]["balance"]:
        print("Insufficient funds.")
        return

    accounts[acc_num]["balance"] -= amt
    record_transaction(acc_num, "Withdrawal", -amt)
    print(f"Withdrew ₹{amt:.2f}. New balance: ₹{accounts[acc_num]['balance']:.2f}")


def view_transactions(acc_num: str) -> None:
    txns = accounts[acc_num]["transactions"]
    if not txns:
        print("No transactions found.")
        return

    print("\nRecent transactions:")
    for txn in txns[-10:]:
        sign = "+" if txn["amount"] >= 0 else ""
        print(f"{txn['time']} | {txn['desc']:12} | {sign}₹{txn['amount']:.2f}")


def change_pin(acc_num: str) -> None:
    old_pin = input("Enter current PIN: ")
    if old_pin != accounts[acc_num]["pin"]:
        print("Incorrect current PIN.")
        return

    new_pin = input("Enter new PIN (4 digits): ")
    confirm = input("Confirm new PIN: ")
    if new_pin != confirm:
        print("PINs do not match.")
        return

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be 4 digits.")
        return

    accounts[acc_num]["pin"] = new_pin
    print("PIN changed successfully.")


def main() -> None:
    print("\n------------ Welcome to the ATM ------------")
    acc_num = input("Enter the account number: ").strip()
    pin = input("Enter the PIN: ").strip()

    if acc_num not in accounts or accounts[acc_num]["pin"] != pin:
        print("Login failed. Invalid account number or PIN.")
        return

    print("Login successful!")

    while True:
        menu()
        ch = input("Enter your choice: ").strip().lower()

        if ch == "c":
            check_balance(acc_num)
        elif ch == "d":
            deposit(acc_num)
        elif ch == "w":
            withdraw(acc_num)
        elif ch == "v":
            view_transactions(acc_num)
        elif ch == "p":
            change_pin(acc_num)
        elif ch == "e":
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()