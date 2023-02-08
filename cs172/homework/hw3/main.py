# File Name:   bank.py
# Purpose:     Main script to simulate a simple bank
# Author:      Tony Kabilan Okeke
# Date:        February 8, 2023 

from bank import Savings, Checking

def showMenu():
    """Show the user the menu"""

    # List of options
    opts = ['Create Savings Account', 'Create Checking Account', 'Deposit', 'Withdraw',
            'Perform End of Month Operations', 'Display Savings Accounts',
            'Display Checking Accounts', 'Display All Accounts', 'Exit']

    # Print the menu
    for i, opt in enumerate(opts):
        print(f'{i + 1}. {opt}')

def createAccount(acctType):
    """Create a new account and validate the input"""

    # Get account info
    name = input("Enter owner's name: ")

    # Validate balance
    prompt = 'Enter initial balance: '
    while True:
        try:
            balance = float(input(prompt))
            if balance < 0:
                prompt = 'Enter a greater than or equal to zero: '
                continue
            break
        except ValueError:
            prompt = 'Invalid input: an float value was expected. Try again: '

    # Create account
    if acctType == 1:
        acc = Savings(name, balance)
    elif acctType == 2:
        acc = Checking(name, balance)
    else:
        raise ValueError('Invalid account type')

    return acc


if __name__ == "__main__":
    # Create list of accounts
    accounts = []
    accountNums = []

    # Get and validate user input
    while True:
        try:
            showMenu();
            choice = int(input('Enter your choice: '))
            if not 1 <= choice <= 9:
                raise ValueError
        except ValueError:
            print('Invalid choice. Try again.\n')
            continue

        if choice in [1, 2]:
            # Print account type
            if choice == 1:  print("Savings Account")
            else:            print("Checking Account")

            # Get account info and create account
            acc = createAccount(choice)

            # Add account to list
            accounts.append(acc)
            accountNums.append(acc.getAccountNumber())
            print('Account added\n')

        elif choice == 3:
            # Get deposit info
            print("Deposit")
            prompt = 'Enter account number: '
            while True:
                try:
                    acc = int(input(prompt))
                    break
                except ValueError:
                    prompt = 'Invalid input: an integer value was expected. Try again: '
                    continue

            # Validate account number
            if acc not in accountNums:
                print("That account number does not exist")
                continue
            else:
                prompt = 'Enter amount to deposit: '
                while True:
                    try:
                        amount = float(input(prompt))
                        if amount < 0:
                            prompt = 'Enter a greater than or equal to zero: '
                            continue
                        break
                    except ValueError:
                        prompt = 'Invalid input: an float value was expected. Try again: '
                        continue
                
            accounts[accountNums.index(acc)].deposit(amount)
        
        elif choice == 4:
            # Get deposit info
            print("Withdraw")
            prompt = 'Enter account number: '
            while True:
                try:
                    acc = int(input(prompt))
                    break
                except ValueError:
                    prompt = 'Invalid input: an integer value was expected. Try again: '
                    continue

            # Validate account number
            if acc not in accountNums:
                print("That account number does not exist")
                continue
            else:
                prompt = 'Enter amount to withdraw: '
                while True:
                    try:
                        amount = float(input(prompt))
                        if amount < 0:
                            prompt = 'Enter a greater than or equal to zero: '
                            continue
                        break
                    except ValueError:
                        prompt = 'Invalid input: an float value was expected. Try again: '
                        continue
                
            accounts[accountNums.index(acc)].withdraw(amount)

        elif choice == 5:
            # Perform end of month operations
            for acc in accounts:
                acc.endOfMonth()
            print("End of month operations have been performed\n")

        elif choice == 6:
            # Display savings accounts
            for acc in accounts:
                if isinstance(acc, Savings):
                    print(acc)
            print()

        elif choice == 7:
            # Display checking accounts
            for acc in accounts:
                if isinstance(acc, Checking):
                    print(acc)
            print()

        elif choice == 8:
            # Display all accounts
            for acc in accounts:
                print(acc)
            print()

        elif choice == 9:
            print("Good-bye!")
            break
