"""
Data Structures Implementations
"""

# =========================== LINEAR DATA STRUCTURES ===========================

class Queue:
    """FIFO Queue"""

    def __init__(self):
        self.__items = []

    def put(self, items):
        # add items to the end of the queue (FIFO, enqueue)
        self.__items.append(items)

    def get(self):
        # remove items from the front of the queue (FIFO, dequeue)
        return self.__items.pop(0)

    def peek(self):
        # check (but not remove) the element at the front
        return self.__items[0]

    def empty(self):
        # check if queue is empty
        return len(self.__items) == 0

    def clear(self):
        # remove all elements from queue
        self.__items = []

    def __str__(self):
        s = ""
        for i in range(0, len(self.__items)):
            s = s + str(self.__items[i]) + "\n"
        return s

    def __len__(self):
        return len(self.__items)


class Stack:
    """LIFO Stack"""

    def __init__(self):
        self.__items = []

    def put(self, items):
        # add items to the top of the stack (LIFO, push)
        self.__items.insert(0, items)

    def get(self):
        # remove items from the top of the stack (LIFO, pop)
        return self.__items.pop(0)

    def peek(self):
        # check (but not remove) the element at the top
        return self.__items[0]

    def empty(self):
        # check if stack is empty
        return len(self.__items) == 0

    def clear(self):
        # remove all elements from stack
        self.__items = []

    def __str__(self):
        s = ""
        for i in range(0, len(self.__items)):
            s = s + str(self.__items[i]) + "\n"
        return s

    def __len__(self):
        return len(self.__items)


class PriorityQueue:
    pass


class LinkedList:
    """Linked List"""

    class Node:
        """Node for a linked list"""

        def __init__(self, data, next=None):
            self.__data = data
            self.__next = next

        def getData(self):
            return self.__data

        def getNext(self):
            return self.__next

        def setData(self, data):
            self.__data = data

        def setNext(self, next):
            self.__next = next

        def __str__(self):
            return f"{self.__data} -> {self.__next}"

    def __init__(self):
        self.__head = None
        self.__tail = None

    def isEmpty(self):
        # Is the list empty?
        return self.__head == None and self.__tail == None

    def __len__(self):
        # Return the number of items in the list
        if self.isEmpty():
            return 0
        elif self.__head == self.__tail:
            return 1
        else:
            count = 1
            current = self.__head
            while current.getNext() != None:
                count += 1
                current = current.getNext()
            return count

    def append(self, data):
        # Add a new node to the end of the list
        temp = LinkedList.Node(data)

        if self.isEmpty():
            self.__head = temp
            self.__tail = temp
        else:
            self.__tail.setNext(temp)
            self.__tail = temp

    def prepend(self, data):
        # Add a new node to the beginning of the list
        temp = LinkedList.Node(data)

        if self.isEmpty():
            self.__head = temp
            self.__tail = temp
        else:
            temp.setNext(self.__head)
            self.__head = temp

    def search(self, item):
        # Search for item in the list
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        # Remove item from the list
        current = self.__head
        previous = None
        found = False

        # Find the item
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        # Remove the item
        if current == None:
            return False
        elif previous == None:
            self.__head = current.getNext()
            return True
        else:
            previous.setNext(current.getNext())
            return True

    def __getitem__(self, index):
        # Return the item at index
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        else:
            current = self.__head
            for i in range(index):
                current = current.getNext()
            return current.getData()

    def __setitem__(self, index, item):
        # Set the item at index
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        else:
            current = self.__head
            for i in range(index):
                current = current.getNext()
            current.setData(item)

    def __str__(self):
        # Return a string representation of the list
        s = ""
        current = self.__head
        while current != None:
            s = s + str(current.getData()) + " -> "
            current = current.getNext()
        s = s + "None"
        return s


class BinarySearchTree:
    class Node:
        """Node for a Binary Search Tree"""

        def __init__(self, value):
            self.__value = value
            self.__left = None
            self.__right = None

        def setLeft(self, left):
            self.__left = left

        def setRight(self, right):
            self.__right = right

        def getLeft(self):
            return self.__left

        def getRight(self):
            return self.__right

        def getValue(self):
            return self.__value

        def __str__(self):
            return f"{self.getRight()} <- {self.getValue()} -> {self.getLeft()}"

    def __init__(self):
        self.__root = None

    def insert(self, value):
        # Insert a value into the tree

        ## Create new node
        node = BinarySearchTree.Node(value)

        ## If tree is empty, set root to new node
        if self.__root == None:
            self.__root = node
            return

        ## Otherwise, find the correct place to insert the node
        current = self.__root
        while True:
            ## If value is less than current node, go left
            if value <= current.getValue():
                if current.getLeft() == None:  # Leaf node
                    current.setLeft(node)
                    return
                else:
                    current = current.getLeft()

            ## If value is greater than current node, go right
            else:
                if current.getRight() == None:  # Leaf node
                    current.setRight(node)
                    return
                else:
                    current = current.getRight()

    def search(self, value):
        # Search for a value in the tree
        current = self.__root
        while current != None:
            if current.getValue() == value:
                return True
            elif value < current.getValue():
                current = current.getLeft()
            else:
                current = current.getRight()
        return False

    def __str__(self):
        if self.__root == None:
            return "Empty tree"
        else:
            current = self.__root
            return str(current)


class HashTable:
    """
    This implementation uses a list of lists to represent the hash table, where each element in 
    the outer list corresponds to a bucket, and each element in the inner lists is a key-value 
    pair. The `_hash` function takes in a `key` string and uses the `ord` function to generate a 
    hash value, which is then modded by the size of the hash table to get an index. The `add` 
    function takes a `key` string and a `value` of any type and hashes the key to find an index in
    the table, then searches for the key in the bucket. If the key already exists, it updates the 
    value. If the key does not exist, it appends a new key-value pair to the bucket list. The 
    `get` function takes a `key` string, hashes it to find the index, and searches the 
    corresponding bucket for the key. If the key is found, it returns the associated value. If the
    key is not found, it raises a `KeyError`. The `remove` function takes a `key` string, hashes 
    it to find the index, and searches the corresponding bucket for the key. If the key is found, 
    it removes the key-value pair from the bucket. If the key is not found, it raises a 
    `KeyError`. 
    Once you have the `HashTable` class, you can use it to create a dictionary like this:
    ```
    my_dict = HashTable()
    my_dict.add("apple", 5)
    my_dict.add("banana", 8)
    my_dict.add("cherry", 3)
    print(my_dict.get("apple")) # 5
    print(my_dict.get("banana")) # 8
    print(my_dict.get("cherry")) # 3
    my_dict.remove("banana")
    print(my_dict.get("banana")) # raises KeyError
    ```
    """

    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def _hash(self, key: str) -> int:
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size
    
    def add(self, key: str, value: any):
        index = self._hash(key)
        # Check if key already exists
        for item in self.table[index]:
            if item[0] == key:  # Key already exists
                item[1] = value
                return
        self.table[index].append((key, value))
    
    def get(self, key: str) -> any:
        index = self._hash(key)
        for item in self.table:
            if item[0] == key:
                return item[1]
        raise KeyError(key)
    
    def remove(self, key: str):
        index = self._hash(key)
        for i, item in enumerate(self.table):
            if item[0] == key:
                del self.table
                return
        raise KeyError(key)
    

