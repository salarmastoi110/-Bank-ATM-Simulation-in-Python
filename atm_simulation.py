# ATM Simulation

# Sample user database (username: PIN)
users = {
    "salaar": {"pin": "1234", "balance": 5000},
    "fatima": {"pin": "4321", "balance": 10000}
}

# Login function
def login():
    print("💳 Welcome to Bank ATM 💳")
    username = input("Enter username: ")
    pin = input("Enter 4-digit PIN: ")

    if username in users and users[username]["pin"] == pin:
        print(f"\n✅ Login successful. Welcome, {username}!\n")
        return username
    else:
        print("❌ Invalid username or PIN.")
        return None

# Menu display
def show_menu():
    print("\n---- ATM Menu ----")
    print("1. Balance Check")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

# Balance check
def check_balance(user):
    print(f"💰 Your current balance is: Rs {users[user]['balance']}")

# Deposit
def deposit(user):
    amount = int(input("Enter amount to deposit: Rs "))
    if amount > 0:
        users[user]['balance'] += amount
        print(f"✅ Rs {amount} deposited successfully.")
        check_balance(user)
    else:
        print("❌ Invalid amount.")

# Withdraw
def withdraw(user):
    amount = int(input("Enter amount to withdraw: Rs "))
    if 0 < amount <= users[user]['balance']:
        users[user]['balance'] -= amount
        print(f"✅ Rs {amount} withdrawn successfully.")
        check_balance(user)
    else:
        print("❌ Insufficient balance or invalid amount.")

# Main program
def atm():
    user = login()
    if user:
        while True:
            show_menu()
            choice = input("Select an option (1-4): ")

            if choice == '1':
                check_balance(user)
            elif choice == '2':
                deposit(user)
            elif choice == '3':
                withdraw(user)
            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break
            else:
                print("❌ Invalid option. Please choose again.")

# Run the ATM simulation
if __name__ == "__main__":
    atm()
