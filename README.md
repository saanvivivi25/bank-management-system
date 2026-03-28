 Bank Management System (Menu-Driven Program)

This is a simple menu-driven Bank Management System implemented in Python. The program simulates basic banking operations such as account creation, deposits, withdrawals, and interest calculation using an in-memory data structure.

> Features

1.Account Creation
Generates a unique account number automatically.
Supports Savings account (Current account is under development).
Enforces a minimum balance requirement.

2.Deposit
Allows users to deposit money into an existing account.
Updates and displays the new balance instantly.

3.Withdraw
Enables withdrawal while ensuring the minimum balance is maintained.
Prevents transactions that violate balance rules.

4.Check Balance
Displays account holder details including name, account type, and balance.

5.Display All Accounts
Lists all accounts stored in the system with their details.

6.Apply Interest
Applies a fixed interest rate to Savings accounts.
Updates balance after adding interest.

7.Exit Option
Allows users to safely terminate the program.

> How It Works
The system uses a dictionary (accounts) to store account details such as:
Account holder name
Balance
Account type
A menu-driven loop continuously prompts the user to select operations until they choose to exit.
Account numbers are randomly generated and ensured to be unique.

> Rules & Constraints
Minimum balance required: 500.0
Interest rate for Savings accounts: 7.25%
Withdrawals cannot reduce balance below the minimum limit.
Interest is applied only to Savings accounts.

> Concepts Used
Functions
Dictionaries
Loops (while loop for menu)
Conditional statements
Random number generation
Basic input/output handling
> Note
This system stores data temporarily (in memory), so all account information will be lost once the program is terminated.
The Current account feature is not yet implemented.
