# File Name:   main.py
# Purpose:     Main script for HW2
# Author:      Tony Kabilan Okeke
# Date:        January 25, 2023

# Import money class
from money import Money


def menu() -> int:
    """Show the menu to the user and validate input"""

    # Define menu options
    idx = range(1,5)
    opt = ['Deposit', 'Withdraw', 'See current balance', 'Exit']

    # Collect and validate input
    while True:
        try:
            # Print menu
            for i, o in zip(idx, opt):  print(f"{i}. {o}")

            # Get user input
            selected = int(input('Enter your choice: '))

            if not 1 <= selected <= 4:
                print('Invalid choice. Try again.\n')
            else:
                break
        except Exception as E:
            print(f'Invalid choice. Try again.\n')

    return selected


def validate(prompt: str, limits: tuple) -> int:
    """Validate user inputs"""

    while True:
        try:
            value = int(input(prompt))
            if not limits[0] <= value <= limits[1]:
                print(f'Error: you entered a value out of range. Try again.')
                prompt = f'Enter a value between {limits[0]} and {limits[1]}: '
            else:
                break
        except Exception as E:
            prompt = 'Invalid input: an integer value was expected. Try again:'

    return value


def inputAmount() -> Money:
    """Collect input from user for dollar amount and return a Money object"""

    dollars = validate('Enter the dollar amount: ', (0, 1000))
    cents = validate('Enter the cents amount: ', (0, 99))
    return Money(dollars, cents)


# Main script
if __name__ == '__main__':

    # Keep track of account balance
    balance = Money()

    while True:
        # Prompt user
        selected = menu()
        print()

        if selected == 1:
            # Print selected option
            print('Deposit')

            # Withdraw specified amount
            balance += inputAmount()
            print(f'Transaction completed.\n')

        elif selected == 2:
            # Print selected option
            print('Withdraw')

            # Store deposit
            withdraw = inputAmount()
            if withdraw > balance:
                print('You do not have enough funds.\n')
            else:
                balance -= withdraw
                print('Transaction completed.\n')

        elif selected == 3:
            # Print current balance
            print(f'Your current balance is: {balance}\n')

        else:
            print('Good-bye!')
            break

