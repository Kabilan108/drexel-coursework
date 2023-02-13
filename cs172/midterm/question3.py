# CS 172 - Midterm Question 3 (Zybooks 15.4)
# Purpose: Implementation of classes for real estate properties
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.13.2023

from abc import ABC, abstractmethod


class Property(ABC):
    """Abstract Base Class for Real Estate Properties"""

    def __init__(self, owner: str, address: str, squareFootage: int, value: float):
        """Class constructor"""
        self.__owner = owner
        self.__address = address
        self.__squareFootage = squareFootage
        self.__value = value

    def getOwner(self):
        """Getter for __owner"""
        return self.__owner
    
    def getAddress(self):
        """Getter for __address"""
        return self.__address
    
    def getSquareFootage(self):
        """Getter for __squareFootage"""
        return self.__squareFootage
    
    def getValue(self):
        """Getter for __value"""
        return self.__value
    
    def setOwner(self, owner):
        """Setter for __owner"""
        self.__owner = owner

    def setValue(self, value):
        """Setter for __value"""
        self.__value = value

    def __str__(self):
        """String Representation"""
        return (f"Address: {self.getAddress()}\n"
                f"Owner: {self.getOwner()}\n"
                f"Square Feet: {self.getSquareFootage()}\n"
                f"Value: ${self.getValue():.2f}")

    @abstractmethod
    def calculatePropertyTaxes():
        """Calculate Property Taxes"""
        pass


class Residential(Property):
    """Implementation of derived class for Residential properties"""

    def __init__(self, owner: str, address: str, squareFootage: int, 
                 value: float, residenceType: str):
        """Class constructor"""
        super().__init__(owner, address, squareFootage, value)
        self.__residenceType = residenceType

    def getResidenceType(self):
        """Getter for __residenceType"""
        return self.__residenceType
    
    def calculatePropertyTaxes(self):
        """Calculate Property taxes"""
        return 1.05/100 * self.getValue()
    
    def __str__(self):
        """String representation"""
        txt = super().__str__()
        return txt + f'\nType: {self.getResidenceType()}'


class Commercial(Property):
    """Implementation of derived class for commercial properties"""

    def __init__(self, owner: str, address: str, squareFootage: int, 
                 value: float, annualProfit: float=0.0):
        """Class constructor"""
        super().__init__(owner, address, squareFootage, value)
        self.__annualProfit = annualProfit

    def getAnnualProfit(self):
        """Getter for __annualProfit"""
        return self.__annualProfit
    
    def setAnnualProfit(self, profit):
        """Setter for __annualProfit"""
        self.__annualProfit = profit
    
    def calculatePropertyTaxes(self):
        """Calculate Property taxes"""
        return self.getValue() / 100 * 6.5542
    
    def __str__(self):
        """String representation"""
        txt = super().__str__()
        return txt + f'\nAnnual profit: ${self.getAnnualProfit():.2f}'
