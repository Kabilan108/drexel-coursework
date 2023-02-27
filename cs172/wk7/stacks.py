#File:     stacks.py
#Purpose:  implement our version of a stack (LIFO)
#Author:   Adelaida A. Medlock
#Date:     2/16/2021

class MyStack():
    
    # constructor
    def __init__(self):
        self.__theList = []
    
    # overloaded operators
    def __str__(self):
        s = ''
        for i in range(0, len(self.__theList)) :
            s = s + str(self.__theList[i]) + '\n'
        return s
    
    def __len__(self):
        return( len(self.__theList) )
    
    # add elements to the top of the stack
    def put(self, item):
        self.__theList.insert(0, item)
    
    # remove elements from the top of the stack
    def get(self):
        a = self.__theList.pop(0)
        return a
    
    # remove all elements from the stack
    def clear(self):
        self.__theList = [] 
    
    # check (but not remove) the element at the top
    def peek(self):
        return self.__theList[0]
    
    # check if stack is empty    
    def empty(self):
        if len(self.__theList) == 0:
            return True
        else:
            return False


# Testing our stack implementation
if __name__ == '__main__' :
    
    print('Testing our stack implementation')
    print('--------------------------------')
    
    # create a display a new stack
    deck = MyStack()
    print('Here is our empty stack:')
    print(deck)
    
    # add a few values
    deck.put('10 of Spades')
    deck.put('5 of Diamonds')
    deck.put('Queen of Hearts')
    deck.put('Ace of Clubs')
    
    # display stack again
    if not deck.empty() :
        print('Here is our deck after adding a few cards:')
        print(deck)
        
        print('There are', len(deck), 'cards in the deck.\n')
    
        # get a card from the stack
        first = deck.get()  # get top element from the stack
        print('Taking a card from the top of the deck: ', end = ' ')
        print(first)
        
        # peek to see which is the value at the top of stack
        print('The current card at the top of the deck is: ', end = ' ')
        print(deck.peek())
    
        print('\nHere is our deck after taking the first card:')
        print(deck)
    
