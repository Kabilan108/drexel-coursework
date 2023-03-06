# File Name: employee.py
# Purpose:   This script implements the Employee class
# Author:    Tony Kabilan Okeke
# Date:      March 5, 2023


class Employee:
    """
    This class represents an employee
    """

    # Static employee counter
    __employeeCount = 1


    def __init__(self, name, rate=0.0):
        """This method initializes the Employee class"""

        self.__name = name
        self.__rate = rate
        self.__hours = 0.0
        self.__EID = Employee.__employeeCount
        Employee.__employeeCount += 1

    def getRate(self):
        """This method returns the employee's hourly rate"""

        return self.__rate

    def getEID(self):
        """This method returns the employee's employee ID"""

        return self.__EID

    def getName(self):
        """This method returns the employee's name"""

        return self.__name

    def getHours(self):
        """This method returns the employee's hours worked"""

        return self.__hours

    def getGrossPay(self):
        """This method returns the employee's gross pay"""

        return self.__hours * self.__rate

    def setRate(self, rate):
        """This method sets the employee's hourly rate"""

        self.__rate = rate

    def setHours(self, hours):
        """This method sets the employee's hours worked"""

        self.__hours = hours

    def __eq__(self, ID):
        """Compare the employee ID to the given ID""" 

        return self.__EID == ID

    def __str__(self) -> str:
        """Return a string representation of the object"""

        repr  = f"Employee Name: {self.getName()}\n"
        repr += f"Employee ID: {self.getEID()}\n"
        repr += f"Hourly Rate: {self.getRate():.2f}\n"
        repr += f"Hours Worked: {self.getHours():.2f}\n"
        repr += f"Gross Pay: {self.getGrossPay():.2f}"
        return repr

