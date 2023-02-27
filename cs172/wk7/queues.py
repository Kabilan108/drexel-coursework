#File:     queues.py
#Purpose:  implement our  version of a queue (FIFO)
#Author:   Adelaida A. Medlock
#Date:     2/16/2021

class MyQueue():
    
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
    
    # add elements to the end of the queue
    def put(self, item):
        self.__theList.append(item)
    
    # remove elements from the front of the queue
    def get(self):
        a = self.__theList.pop(0)
        return a
    
    # remove all elements from queue
    def clear(self):
        self.__theList = []
    
    # check (but not remove) the element at the front
    def peek(self):
        return self.__theList[0]
    
    # check if queue is empty    
    def empty(self):
        if len(self.__theList) == 0:
            return True
        else:
            return False


# Testing our queue implementation
if __name__ == '__main__' :
    
    print('Testing our queue implementation')
    print('--------------------------------')
    
    # create a display a new queue
    line = MyQueue()
    print('Here is our empty queue:')
    print(line)
    
    # enqueue a few items
    line.put('Mary')
    line.put('John')
    line.put('Rose')
    line.put('Bob')
    
    # process the queue
    if not line.empty() :
        print('Here is our queue after adding a few people:')
        print(line)
        
        print('There are', len(line), 'people in the queue.\n')
    
        # dequeue an item from the queue
        first = line.get()  # get first item from the queue
        print('First in line: ', end = ' ')
        print(first)
        
        # peek to see which is the item at the front of queue
        print('After dequeueing first person, next in line is: ', end = ' ')
        print(line.peek())
    
        print('\nHere is our queue after dequeing first person:')
        print(line)
    
