# Creating Classes and Overloading Operators

Define a class Money to represent a money amount (with dollars and cents, for example 
10.05). All Money objects have two data members:

- dollars: an integer value greater than or equal to 0
- cents: an integer value between 0 and 99

For this class provide

- a constructor: assume that if not data is provided, dollars and cents are both equal 
  to zero.
- inspectors/getters for both data members. Use the get convention to name your getters.
- mutators/setters for both data members:
  - addDollars(): modifies the Money object by adding a given amount of dollars.
  - addCents(): modifies the Money object by adding a given amount of cents.

Then proceed to overload the following operators:

- The addition (+) operator so we can add two Money objects. For example the result of 
  3.50 + 10.99 would be 14.99.
- The subtraction (-) operator so can subtract one Money object from another Money 
  object. This operator returns a Money object that represents the difference between 
  two Money objects. For example the result of both 3.50 - 10.99 and 10.99 - 3.50 
  would be 7.49.
- The multiplication (*) operator. This operator will be used to multiply a Money 
  object by an integer value. For example the result of 3.50 * 2 would be 7.00.
- The __str__ special method, so the print function can be used with this class. Money 
  objects must be displayed wit the $ sign, and two decimal places after the decimal 
  point. For example: $7.49, $33.00, and $10.05
- The comparison operators: ==, !=, <, <=, > and >=
- The subscript operator ([]), as an accessor.

The code for the Money class should be saved in the money.py file.

In the main.py file you will have the main script for this assignment. We are 
simulating a very simple bank account. Here are some additional specifications:

- Your program should keep track of the current balance in the account. Create a 
  Money object to keep track of the balance in the account. Assume the initial balance 
  is $0.00.

- Your program should present a menu to the user with the following options:
  1. Deposit
  2. Withdraw
  3. See current balance
  4. Exit

- Option 1 allows the user to deposit money in the account. The program should ask the 
  user to enter the dollar and cents parts of a Money object, create a new Money object 
  and update the current balance.
  - Remember that cents can only be a number between 0 and 99. This input must be 
    validated.
  - Dollars can be any value 0 and above, but for this program we will accept values 
    between 0 and 1000. This input must be validated.

- Option 2 allows the user to withdraw an amount of money from the account. The 
  program should ask the user to enter the dollar and cents parts of a Money object 
  (perform the same input validation as in Option 1), create a Money object and then 
  check if there are enough funds in the account balance (hint: you must use the 
  comparison operators here).
  - If there are enough funds in the account, update the balance. Otherwise, let the 
    user know that there are not enough funds in the account.

- Option 3 displays the current balance in the account.

- Option 4 allows the user to exit the program.

- Your program must have a function that validates a value entered by the user to make 
  sure the value is an integer and within a desired range. If the user does not enter 
  a valid value, the function should repeatedly ask the user for a value, until a 
  valid one is provided. This function returns a valid integer value entered by the 
  user.

Below there’s a sample run:

```
1. Deposit
2. Withdraw
3. See current balance
4. Exit
Enter your choice: 3

Your current balance is: $0.00

1. Deposit
2. Withdraw
3. See current balance
4. Exit
Enter your choice: 1

Deposit
Enter the dollar amount: 10
Enter the cents amount: 5
Transaction completed.

1. Deposit
2. Withdraw
3. See current balance
4. Exit
Enter your choice: 3

Your current balance is: $10.05

1. Deposit
2. Withdraw
3. See current balance
4. Exit
Enter your choice: 2

Withdraw
Enter the dollar amount: 3
Enter the cents amount: 77
Transaction completed.

1. Deposit
2. Withdraw
3. See current balance
4. Exit
Enter your choice: 3

Your current balance is: $6.28

1. Deposit
2. Withdraw
3. See current balance
4. Exit
Enter your choice: 4

Good-bye!
```

