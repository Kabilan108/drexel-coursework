# File Name: main.py
# Purpose:   Main script for the payroll simulator
# Author:    Tony Kabilan Okeke
# Date:      March 5, 2023

from linkedList import Node, LinkedList
from employee import Employee


def showMenu():
    """Show the menu of options to the user"""

    opts = ["Add New Employee", "Enter Employee Hours", "Update Employee Hourly Rate",
            "Display Payroll", "Remove Employee from Payroll", "Exit the program"]
    keys = ['a', 'b', 'c', 'd', 'e', 'f']

    for opt, key in zip(opts, keys):
        print(f"{key}. {opt}")

    choice = input("Enter your choice: ")

    return choice


if __name__ == '__main__':
    
    # Create a linked list
    employees = LinkedList()

    # Welcome message
    print("*** CS 172 Payroll Simulator ***")

    while True:
        # Show the menu
        choice = showMenu()

        if choice == 'a':  # Add a new employee
            name = input("Enter the new employee name: ")
            rate = float(input("Enter their hourly rate: "))
            emp = Employee(name, rate)
            employees.append(emp)
            print(f"Employee {emp.getEID()} added to payroll")

        elif choice == 'b':  # Enter employee hours
            N = len(employees)

            for i in range(N):
                eid = employees[i].getEID()
                hours = float(input(f"Enter hours worked for employee {eid}: "))
                employees[i].setHours(hours)

        elif choice == 'c':  # Update employee hourly rate
            eid = int(input("Enter employee ID: "))
            emp = employees.search(eid)
            if emp is None:
                print("Employee doesn't exist.")
            else:
                rate = float(input(f"Enter new wage for employee {eid}: "))
                emp.setRate(rate)

        elif choice == 'd':  # Display payroll
            N = len(employees)
            
            print("*** Payroll ***")
            for i in range(N):
                print(employees[i])

        elif choice == 'e':  # Remove employee from payroll
            eid = int(input("Enter employee ID: "))
            emp = employees.search(eid)

            if emp is None:
                print("Employee doesn't exist.")
            else:
                employees.remove(emp)

        elif choice == 'f':  # Exit the program
            print("Goodbye.")
            break

        else:
            print("Invalid entry.")

