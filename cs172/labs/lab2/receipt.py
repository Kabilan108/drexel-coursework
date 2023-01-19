# CS 172 - Lab 1
#
# Description: This module contains the definition of the receipt class.
#
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.19.2023

# Imports
from datetime import datetime
from item import Item


class Receipt:
    """
    Reciept Class

    Attributes
    ----------
    __tax_rate : float
        Tax rate in the area
    __purchases : list
        A list of items purchased

    Methods
    -------
    recieptToString() -> str
        Returns the full receipt as a string
    addItem(item : Item) -> None
        Adds an item to the receipt
    """

    def __init__(self, taxrate: float = 0.07) -> None:
        """Receipt Constructor"""

        # Define attributes
        self.__tax_rate = taxrate
        self.__purchases = []

    def receiptToString(self) -> str:
        """Returns the full receipt as a string"""

        # Receipt header with date and time
        # reciept = f"---- Receipt {datetime.now()} ----\n"
        # Use this header for Zybooks
        reciept = f"----- Receipt time -----\n"

        # Add items to the reciept and calculate the tax and subtotal
        tax = 0
        subtotal = 0
        for item in self.__purchases:
            reciept += f"{item.itemToString()}\n"
            tax += item.getTax(self.__tax_rate)
            subtotal += item.getPrice()

        # Format text for subtotal, tax and total
        total = f"{subtotal + tax:.2f}"
        subtotal = f"{subtotal:.2f}"
        tax = f"{tax:.2f}"

        # Add the tax and subtotal to the reciept
        reciept += f"\n{'Sub Total':_<20}{subtotal:_>20}\n"
        reciept += f"{'Tax':_<20}{tax:_>20}\n"
        reciept += f"{'Total':_<20}{total:_>20}\n"

        return reciept

    def addItem(self, item: Item) -> None:
        """Adds an item to the receipt"""

        self.__purchases.append(item)

