class ATM:
    def __init__(self, account_balance=0, pin="1234"):
        """Initialize the ATM with an account balance and a PIN."""
        self.account_balance = account_balance
        self.pin = pin
        self.transaction_history = []

    def balance_inquiry(self):
        """Return the current account balance."""
        return self.account_balance

    def cash_withdrawal(self, amount):
        """Withdraw a specified amount from the account if funds are available."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrawal successful: ${amount}"
        else:
            return "Insufficient funds."

    def cash_deposit(self, amount):
        """Deposit a specified amount into the account."""
        self.account_balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return f"Deposit successful: ${amount}"

    def change_pin(self, old_pin, new_pin):
        """Change the PIN if the old PIN is correct."""
        if old_pin == self.pin:
            self.pin = new_pin
            return "PIN changed successfully."
        else:
            return "Incorrect old PIN."

    def transaction_history_inquiry(self):
        """Return the transaction history."""
        return self.transaction_history


def main():
    # Prompt the user for initial account balance and PIN
    initial_balance = float(input("Enter your initial account balance: $"))
    initial_pin = input("Set your initial PIN: ")

    atm = ATM(initial_balance, initial_pin)  # Initialize ATM with user-defined values

    while True:
        print("\nWelcome to the ATM!")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            print(f"Current balance: ${atm.balance_inquiry()}")
        
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.cash_withdrawal(amount))
        
        elif choice == '3':
            amount = float(input("Enter amount to deposit: "))
            print(atm.cash_deposit(amount))
        
        elif choice == '4':
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(old_pin, new_pin))
        
        elif choice == '5':
            history = atm.transaction_history_inquiry()
            if history:
                print("Transaction History:")
                for transaction in history:
                    print(transaction)
            else:
                print("No transactions to display.")
        
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
