    # Global list to store all transactions across accounts
transactions = []

class Account: 
    """
    Represents a bank account with basic operations like withdraw, deposit, transfer
    """
    def __init__(self, name, account_num, pin, balance):
        self.name = name
        self.account_num = account_num
        self.pin = pin
        self.balance = balance
    
    def inquiry(self):
        """Display current account balance"""
        print(f"Your current balance = {self.balance} EGP.")

    def withdraw(self):  
        """Withdraw money from account with validation"""
        try:
            amount = int(input("Enter an amount: "))
            # Check for negative amounts
            if amount <= 0:
                print("Amount must be positive.")
                return
            
            # Check if sufficient balance exists
            if self.balance >= amount:
                self.balance = self.balance - amount
                print(f"Your current balance = {self.balance} EGP")
                self.record_transactions("Withdraw", amount)
            else:
                print(f"Amount is greater than your balance. Your balance = {self.balance} EGP.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    def deposit(self):   
        """Deposit money to account with validation"""
        try:
            amount = int(input("Enter an amount: "))
            # Check for negative or zero amounts
            if amount <= 0:
                print("Amount must be positive.")
                return
            
            self.balance = self.balance + amount
            print(f"Your current balance = {self.balance} EGP")
            self.record_transactions("Deposit", amount)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    def transfer(self):
        """Transfer money to another account with validation"""
        try:
            # Get target account number
            acc_num = int(input("Enter the target account number: "))
            
            # Search for target account
            target_account = None
            for account in accounts:
                if account.account_num == acc_num:
                    target_account = account
                    break
            
            # Check if target account exists
            if target_account is None:
                print("Invalid account number.")
                return
            
            # Check if trying to transfer to same account
            if acc_num == self.account_num:
                print("Cannot transfer to the same account.")
                return
            
            # Get transfer amount
            amount = int(input("Enter an amount to transfer: "))
            
            # Validate amount
            if amount <= 0:
                print("Amount must be positive.")
                return
            
            # Check if sufficient balance exists
            if self.balance >= amount:
                self.balance = self.balance - amount 
                target_account.balance = target_account.balance + amount  # Add money to target account
                print(f"You transferred {amount} EGP to account {acc_num}. Your current balance = {self.balance} EGP")
                self.record_transactions("Transfer", amount)
                # Record transaction for target account as well
                target_account.record_transactions("Received Transfer", amount)
            else:
                print(f"Amount is greater than your balance. Your balance = {self.balance} EGP")        
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def record_transactions(self, type_of_trans, amount):
        """Record transaction in global transactions list"""
        transactions.append(f"{self.name} - {type_of_trans}: {amount} EGP")

    def show_transactions(self):
        """Display last 5 transactions for current account"""
        # Filter transactions for current account
        account_transactions = [trans for trans in transactions if trans.startswith(self.name)]
        
        if len(account_transactions) == 0:
            print("There are no transactions.")
        else:
            # Show last 5 transactions
            last_transactions = account_transactions[-5:]
            print("Your last transactions:")
            for trans in last_transactions:
                print(f"  {trans}")

    def change_pin(self):
        """Change account PIN with validation"""
        try:
            old_pin = int(input("Enter your old PIN: "))
            if old_pin == self.pin:
                new_pin = int(input("Enter your new PIN: "))
                # Basic PIN validation (4 digits)
                if len(str(new_pin)) != 4 or new_pin < 0:
                    print("PIN must be exactly 4 digits.")
                    return
                
                self.pin = new_pin
                print("Your PIN has been successfully changed.")
            else:
                print("Invalid old PIN!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

################ATM CLASS################
class ATM:   
    """
    ATM machine class that handles user authentication and menu operations
    """
    def __init__(self):
        self.current_account = None
    
    def auth(self):
        """Authenticate user with account number and PIN"""
        try:
            acc_num = int(input("Enter your account number: "))
            pin = int(input("Enter your PIN: "))
            
            # Search for matching account
            for account in accounts:
                if account.account_num == acc_num and account.pin == pin:
                    self.current_account = account
                    print(f"\nHello, {account.name}!")
                    return True
            
            print("[ERROR] Invalid account number or PIN.")
            return False
            
        except ValueError:
            print("[ERROR] Invalid input. Please enter valid numbers.")
            return False

    def show_menu(self):
        """Display ATM menu options"""
        print("\n" + "="*40)
        print("           ATM MENU")
        print("="*40)
        print("1 - Inquiry your balance")
        print("2 - Withdraw")
        print("3 - Deposit")
        print("4 - Transfer")
        print("5 - Change PIN")
        print("6 - Show last 5 transactions")
        print("7 - Exit")
        print("="*40)
    
    def exit(self):
        """Exit ATM session"""
        print(f"Goodbye {self.current_account.name}! Thank you for using our ATM.")
        self.current_account = None

# Initialize accounts
accounts = [
    Account("Mahmoud Mohsen", 456789, 1234, 100),
    Account("Ali Ahmed", 987654, 5678, 200)
]

# Create ATM instance
atm = ATM()

def main():
    """Main function to run the ATM system"""
    print("Welcome to the ATM System!")
    
    # Authentication loop
    while True:
        if atm.auth():
            break
        retry = input("Would you like to try again? (y/n): ").lower()
        if retry != 'y':
            print("Thank you for visiting our ATM.")
            return
    
    # Main ATM operations loop
    while True:
        try:
            atm.show_menu()
            option = int(input("Please choose an option from the menu: "))
            
            # Handle menu options
            if option == 1:
                atm.current_account.inquiry()
            elif option == 2:
                atm.current_account.withdraw()
            elif option == 3:
                atm.current_account.deposit()
            elif option == 4:
                atm.current_account.transfer()
            elif option == 5:
                atm.current_account.change_pin()
            elif option == 6:
                atm.current_account.show_transactions()
            elif option == 7:
                atm.exit()
                break
            else:
                print("Invalid option. Please choose a number between 1-7.")
                continue
            
            # Ask if user wants to continue
            print("\n" + "-"*40)
            contin = input("Enter 'y' to continue, 'n' to exit: ").lower()
            if contin == "n":
                atm.exit()
                break
            elif contin != "y":
                print("Invalid input. Continuing...")
                
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nSession terminated by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the ATM system
if __name__ == "__main__":
    main()