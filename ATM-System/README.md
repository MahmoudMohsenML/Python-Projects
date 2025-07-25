# ATM System

A simple command-line ATM (Automated Teller Machine) simulation built in Python that allows users to perform basic banking operations.

## Features

- **Account Authentication**: Secure login with account number and PIN
- **Balance Inquiry**: Check current account balance
- **Cash Withdrawal**: Withdraw money with balance validation
- **Cash Deposit**: Deposit money into account
- **Money Transfer**: Transfer funds between accounts
- **PIN Change**: Update account PIN securely
- **Transaction History**: View last 5 transactions
- **Error Handling**: Comprehensive input validation and error management

## System Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Download the `atm_system.py` file
2. Ensure Python is installed on your system
3. Run the program from command line or terminal

## Usage

### Running the Program

```bash
python atm_system.py
```

### Default Accounts

The system comes with two pre-configured test accounts:

| Account Holder | Account Number | PIN  | Initial Balance |
|---------------|----------------|------|-----------------|
| Mahmoud Mohsen| 456789         | 1234 | 100 EGP         |
| Ali Ahmed     | 987654         | 5678 | 200 EGP         |

### Menu Options

Once authenticated, users can choose from the following options:

1. **Inquiry Balance** - Display current account balance
2. **Withdraw** - Withdraw money from account
3. **Deposit** - Add money to account
4. **Transfer** - Send money to another account
5. **Change PIN** - Update account PIN
6. **Show Transactions** - View last 5 transactions
7. **Exit** - End ATM session

## How to Use

### 1. Authentication
- Enter your account number when prompted
- Enter your 4-digit PIN
- If credentials are incorrect, you'll be asked to try again

### 2. Performing Transactions

#### Withdraw Money
- Select option 2 from menu
- Enter amount to withdraw
- System checks if sufficient balance exists
- Balance is updated and transaction is recorded

#### Deposit Money
- Select option 3 from menu
- Enter amount to deposit
- Money is added to account
- Balance is updated and transaction is recorded

#### Transfer Money
- Select option 4 from menu
- Enter target account number
- Enter amount to transfer
- System validates target account and sufficient balance
- Money is transferred and both accounts are updated

#### Change PIN
- Select option 5 from menu
- Enter current PIN for verification
- Enter new 4-digit PIN
- PIN is updated securely

## Code Structure

### Classes

#### `Account`
Represents a bank account with the following attributes:
- `name`: Account holder's name
- `account_num`: Unique account number
- `pin`: 4-digit PIN for authentication
- `balance`: Current account balance

**Methods:**
- `inquiry()`: Display balance
- `withdraw()`: Withdraw money
- `deposit()`: Add money
- `transfer()`: Transfer to another account
- `change_pin()`: Update PIN
- `show_transactions()`: Display transaction history
- `record_transactions()`: Log transactions

#### `ATM`
Manages ATM operations and user interface:
- `auth()`: Handle user authentication
- `show_menu()`: Display menu options
- `exit()`: End session

### Global Variables
- `transactions[]`: List storing all transaction records
- `accounts[]`: List of available accounts
- `atm`: ATM instance

## Sample Session

```
Welcome to the ATM System!
Enter your account number: 456789
Enter your PIN: 1234

Hello, Mahmoud Mohsen!

========================================
           ATM MENU
========================================
1 - Inquiry your balance
2 - Withdraw
3 - Deposit
4 - Transfer
5 - Change PIN
6 - Show last 5 transactions
7 - Exit
========================================
Please choose an option from the menu: 1
Your current balance = 100 EGP.

----------------------------------------
Enter 'y' to continue, 'n' to exit: n
Goodbye Mahmoud Mohsen! Thank you for using our ATM.
```

## Future Enhancements

Potential improvements that could be added:
- Transaction limits and daily caps
- Account locking after failed attempts
- Database integration for persistent storage
- Receipt generation
- Multi-language support

## Security Notes

- This is a simulation for educational purposes
- In a real ATM system, PINs would be encrypted and the account number is read automatically.
- Account data would be stored securely in databases
- Additional security measures would be implemented

## Contributing

This is a learning project. Feel free to:
- Report bugs or issues
- Suggest improvements
- Fork and enhance the code
- Add new features following the existing structure

## License

This project is for educational purposes. Feel free to use and modify as needed.

---

**Note**: This ATM system is designed for learning Python programming concepts including object-oriented programming, error handling, and user input validation.