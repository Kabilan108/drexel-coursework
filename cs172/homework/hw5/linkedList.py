# File Name: linkedList.py
# Purpose:   This script contains my implementation of a linked list
# Author:    Tony Kabilan Okeke
# Date:      March 5, 2023


class Node:
    """
    This class represents a node in a linked list
    """

    def __init__(self, data, next=None):
        """This method initializes the Node class"""

        self.__data = data
        self.__next = next

    def getData(self):
        """This method returns the data stored in the node"""

        return self.__data

    def getNext(self):
        """This method returns the next node in the linked list"""

        return self.__next

    def setData(self, data):
        """This method sets the data stored in the node"""

        self.__data = data

    def setNext(self, next):
        """This method sets the next node in the linked list"""

        self.__next = next

    def __str__(self):
        """This method returns the string representation of the node"""

        return str(self.__data) + " -> " + str(self.__next)


class LinkedList:
    """
    Implementation of a linked list; a collection of nodes where each node is: data
    and a link to the next node
    """

    def __init__(self):
        """This method initializes the LinkedList class."""

        self.__head = None

    def isEmpty(self):
        """Check if the list is empty."""

        return self.__head == None

    def search(self, data):
        """Search for a node in the linked list"""

        current = self.__head

        while current != None:
            if current.getData() == data:
                return current.getData()
            else:
                current = current.getNext()

        return None

    def append(self, data):
        """Add a node at the end of the linked list"""
        
        next = Node(data)

        # If the list is empty, set the head to the new node
        if self.isEmpty():
            self.__head = next

        # Otherwise, traverse the list until the last node is reached
        else:
            current = self.__head

            while current.getNext() is not None:
                current = current.getNext()

            current.setNext(next)

    def remove(self, data):
        """Remove a node from the linked list"""
        
        current = self.__head
        previous = None
        found =  False

        # Find the item in the list
        while not found and current is not None:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()

        # If the item is not in the list, return False
        if current == None:
            return False
        # Item was in the first node
        elif previous == None:
            self.__head = current.getNext()
            return True
        # Item was in a node other than the first
        else:
            previous.setNext(current.getNext())
            return True

    def __str__(self):
        """Return a string representation of the linked list"""
        
        current = self.__head
        repr = ""

        while current is not None:
            repr += str(current.getData()) + " -> "
            current = current.getNext()

        return repr

    def __len__(self):
        """Return the length of the linked list"""

        current = self.__head
        length = 0

        while current is not None:
            length += 1
            current = current.getNext()

        return length

    def __getitem__(self, index):
        """Return the data at the specified index"""

        if not (0 <= index < len(self)):
            raise IndexError("Index out of range")

        current = self.__head

        for i in range(index):
            current = current.getNext()

        return current.getData()

