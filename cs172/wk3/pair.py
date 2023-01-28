#File Name:   pair.py
#Purpose:     Class to represent a pair in the form (int, int)
#Author:      Adelaida Medlock
#Date:        April 5, 2022

class Pair:
    # constructor
    def __init__(self, a = 1, b = 1):
        self.__a = a
        self.__b = b
    
    # getters
    def getA(self) :
        return self.__a
    
    def getB(self) :
        return self.__b
    
    # setters
    def setA(self, value):
        self.__a = value

    def setB(self, value):
        self.__b = value
        
    # overloaded operators
    def __str__(self):
        return '(' + str(self.__a) + ', ' + str(self.__b) + ') '
    
    def __getitem__(self, loc) :
        if loc == 0:
            return self.__a
        elif loc == 1:
            return self.__b
        else:
            raise Exception('Invalid index')
        
    def __setitem__(self, loc, value) :
        if loc == 0:
            self.__a = value
        elif loc == 1:
            self.__b = value
        else:
            raise Exception('Invalid index')
        
        
    def __floordiv__(self, other):
        a = self.__a // self.__b
        b = other.getA() // other.getB()
        return Pair(a, b)

# test script
if __name__ == "__main__":
    p1 = Pair(10, 2)
    p2 = Pair(20)
    print('Pair 1', p1)
    print('Pair 2', p2)
    print('p1 // p2 =', p1 // p2)
    left = p1[0]
    right = p1[1]
    print('p1 left:', left)
    print('p1 right:', right)
    p2[0] = 100
    p2[1] = 100
    print(p2)
    