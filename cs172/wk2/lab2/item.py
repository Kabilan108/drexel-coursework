# CS 172 - Lab 1
#
# Description: This module contains the definition of the Item class for use with the
#              reciept class.
#
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.19.2023


class Item:
    """
    Item Class
    
    Attributes
    ----------
    __name : str
        Item name
    __price : float
        Item price in dollars
    __taxable : bool
        Is the item taxed?

    Methods
    -------
    itemToString() -> str
        Return the item as a string
    getPrice() -> float
        Returns the price of the item
    getTax() -> float
        Returns the tax charged on the item
    """

    def __init__(self, name: str, price: float, taxable: bool) -> None:
        """Item Constructor"""

        # Define attributes
        self.__name = name
        self.__price = price
        self.__taxable = taxable

    def itemToString(self) -> str:
        """Returns the item as a string"""

        # Construct a string of the item
        price = f"{self.__price:.2f}"
        return f"{self.__name:_<20}{price:_>20}"

    def getPrice(self) -> float:
        """Returns the price of the item"""

        return self.__price

    def getTax(self, taxrate: float) -> float:
        """Returns the tax charged on the item"""

        # Return the tax is the item is taxable, else return 0
        return self.__price * taxrate if self.__taxable else 0

