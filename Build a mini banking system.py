class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, initial_balance=0):
        if owner in self.accounts:
            print("Account already exists.")
            return
        self.accounts[owner] = BankAccount(owner, initial_balance)
        print(f"Account created for {owner}.")

    def get_account(self, owner):
        return self.accounts.get(owner)

    def list_accounts(self):
        if not self.accounts:
            print("No accounts available.")
            return
        print("\nAccounts:")
        for owner, account in self.accounts.items():
            print(f"- {owner}: ${account.balance:.2f}")


def main():
    bank = BankingSystem()

    while True:
        print("\n=== Mini Banking System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. List Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            bank.create_account(name, balance)

        elif choice == "2":
            name = input("Enter account holder name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            name = input("Enter account holder name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            name = input("Enter account holder name: ")
            account = bank.get_account(name)
            if account:
                account.check_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            bank.list_accounts()

        elif choice == "6":
            print("Thank you for using the Mini Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()