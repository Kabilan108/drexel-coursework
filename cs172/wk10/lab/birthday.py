# File Name: birthday.py
# Purpose:   Implementation of Birthday object (Hash Table)
# Author:    Tony Kabilan Okeke <tko35@drexel.edu>
# Date:      March 16, 2023


class Birthday:
    """Birthday Hash Table Object"""

    def __init__(self, month, day, year):
        """Constructor"""
        self.__month = month
        self.__day = day
        self.__year = year

    def getMonth(self):
        """Return the month"""
        return self.__month

    def getDay(self):
        """Return the day"""
        return self.__day

    def getYear(self):
        """Return the year"""
        return self.__year

    def __str__(self):
        """String representation of Birthday object"""
        return f"{self.__month}/{self.__day}/{self.__year}"

    def __hash__(self):
        """Hash method"""
        return (self.__day + self.__month + self.__year) % 12

    def __eq__(self, other):
        """Equality method"""
        return (self.__day == other.__day and 
                self.__month == other.__month 
                and self.__year == other.__year)

