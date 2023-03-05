#Program:     BST_Implementation.py
#Purpose:     Basic implementation of a Binary Searth Tree (BST)
#Author:      Adelaida Medlock
#Date:        March 3, 2021

# Node class -- this is the basic element of a BST
class Node():
    # constructor
    def __init__(self, value):
        self.__value = value
        self.__right = None
        self.__left = None
    
    # setters
    def setLeft(self, l):
        self.__left = l
            
    def setRight(self, r):
        self.__right = r
    
    # getters
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def getValue(self):
        return self.__value
    
    # overloaded operators
    def __str__(self):
        nodeStr = 'The data in this node is ' + str(self.__value) + ' '
        nodeStr =  nodeStr + 'Its left child is located at ' + str(self.__left) + ' '
        nodeStr =  nodeStr + 'Its right child is located at ' + str(self.__right) + ' '
        return nodeStr


# BST class - basic implementation of a Binary Search Tree
class BST():
    # constructor
    def __init__(self):
        self.__root = None
    
    # setter: insert a new node in the tree
    def insert(self, value):
        # create new node with value
        node = Node(value)
        
        # if BST is empty, the new node is the root
        if self.__root == None:
            self.__root = node
            return 
        
        # if BST is not empty, find the proper place for the new node
        current = self.__root
        while True:
            # new node is going to be on the left of current node
            if value <= current.getValue():
                if current.getLeft() == None:  # we have a leaf, insert new node
                    current.setLeft(node)
                    return
                else:
                    current = current.getLeft()
             
             # new node is going to be on the right of current node
            else:
                if current.getRight() == None: # we have a leaf, insert new node
                    current.setRight(node)
                    return
                else:
                    current = current.getRight()

    # search method
    def search(self, value):
        # empty BST - the value is not there
        if self.__root == None:
            return False
        
        # BST is not empty. Traverse and see if value is there
        current = self.__root
        while current != None:  # keep going as long as we haven't reached the last node
            if current.getValue() == value:
                return True
            elif value < current.getValue():  # search to the left
                current = current.getLeft()
            else:
                current = current.getRight()  # search to the right
        
        # value was not in the BST
        return False
     
     
    # overloaded operator 
    def __str__(self):
        if self.__root != None :
            current = self.__root
            sVal = 'The Root of the tree is ' + str(current.getValue()) + ' '
            sVal = sVal + '\nTo the left of the Root we have: '
            sVal = sVal + '(' + str(current.getLeft())
            #sVal = sVal + ' The Root of the tree is ' + str(current.getValue()) + ' '
            sVal = sVal + ') \nTo the right of the Root we have: ('
            sVal = sVal + str(current.getRight()) + ')'
        return sVal

# Testing BST implementation
if __name__ == "__main__":
    # values to be inserted in the tree
    values = [2, 3, 4, 1, 5, 2]
    
    #empty new BST
    tree = BST() #empty new BST
    
    # insert values in the list into the BST, one at the time
    for value in values:
        print('Inserting: ', value)
        tree.insert(value)
    print()
    
    # searching for a value in the BST
    value = int(input('Enter value to search: '))
    print(tree.search(value))
    print()
    
    # print the BST
    print(tree)
   

        
