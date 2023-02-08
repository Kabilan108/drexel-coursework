# File Name:   bank.py
# Purpose:     Implementation of bank classes
# Author:      Tony Kabilan Okeke
# Date:        February 5, 2023

from abc import ABC, abstractmethod


class BankAccount(ABC):
    """
    Abstract Base Class for Bank Accounts
    """

    # Static attribute to count account numbers
    __nextAccountNumber = 1000

    def __init__(self, owner, balance=0.0):
        """Class constructor"""
        self.__owner = owner
        self.__balance = balance
        self.__accountNumber = BankAccount.getNextAccountNumber()

    def getOwner(self):
        """Returns the name of the account owner"""
        return self.__owner

    def getBalance(self):
        """Returns the current balance in the account"""
        return self.__balance

    def getAccountNumber(self):
        """Returns the account number"""
        return self.__accountNumber

    def deposit(self, amount):
        """Increases the balance by the amount"""
        self.__balance += amount

    def withdraw(self, amount):
        """Decreases the balance by the amount"""
        # Check if the amount is greater than the balance
        if amount > self.__balance:
            print("You do not have enough funds")
            return
        self.__balance -= amount

    def __eq__(self, other):
        """Overload the equality operator"""
        return self.getAccountNumber() == other.getAccountNumber()

    def __str__(self):
        """Returns a string representation of the account"""
        return (f"Account Number: {self.getAccountNumber()}\n"
                f"Account Owner: {self.getOwner()}\n"
                f"Account Balance: ${self.getBalance():.2f}")

    @staticmethod
    def getNextAccountNumber():
        """Returns the next available account number should start at 1000"""
        accountNumber = BankAccount.__nextAccountNumber
        BankAccount.__nextAccountNumber += 1
        return accountNumber

    @abstractmethod
    def endOfMonth(self):
        """Abstract method"""
        pass


class Savings(BankAccount):
    """
    Savings Account Class
    """

    def __init__(self, owner, balance=0.0, interestRate=3.25):
        """Class constructor"""
        super().__init__(owner, balance)
        self.__interestRate = interestRate

    def getInterestRate(self):
        """Returns the interest rate"""
        return self.__interestRate

    def setInterestRate(self, interestRate):
        """Sets the interest rate"""
        self.__interestRate = interestRate

    def __eq__(self, other):
        """Overload the equality operator"""
        return self.getAccountNumber() == other.getAccountNumber()

    def __str__(self):
        """Returns a string representation of the account"""
        return (f"Account Number: {self.getAccountNumber()}\n"
                f"Account Owner: {self.getOwner()}\n"
                f"Account Balance: ${self.getBalance():.2f}\n"
                f"Annual Interest Rate: {self.getInterestRate()}%")

    def endOfMonth(self):
        """Calculates the interest earned and updates the balance"""
        interestrate = self.getInterestRate() / 12
        interest = self.getBalance() * interestrate / 100
        self.deposit(interest)
        return f"Interest earned: ${interest:.2f}"


class Checking(BankAccount):
    """
    Checking Account Class
    """

    def __init__(self, owner, balance=0.0):
        """Class constructor"""
        super().__init__(owner, balance)
        self.__transactions = 0

    def getTransactionsNum(self):
        """Returns the number of transactions"""
        return self.__transactions

    def deposit(self, amount):
        """Increases the balance by the amount"""
        super().deposit(amount)
        self.__transactions += 1

    def withdraw(self, amount):
        """Decreases the balance by the amount"""
        super().withdraw(amount)
        self.__transactions += 1

    def __eq__(self, other):
        """Overload the equality operator"""
        return self.getAccountNumber() == other.getAccountNumber()

    def __str__(self):
        """Returns a string representation of the account"""
        return (f"Account Number: {self.getAccountNumber()}\n"
                f"Account Owner: {self.getOwner()}\n"
                f"Account Balance: ${self.getBalance():.2f}\n"
                f"Transactions this month: {self.getTransactionsNum()}")

    def endOfMonth(self):
        """Determines if the service fee needs to be applied"""
        if self.getTransactionsNum() > 7:
            self.withdraw(5)
        self.__transactions = 0
