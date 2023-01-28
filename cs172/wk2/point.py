##File Name:  point.py
#Purpose:     Class to represent a point located at coordinates x, y
#Author:      Adelaida Medlock
#Date:        January 16, 2021

import math

class Point:
    # static attribute
    __count = 0  # to count how many points we have created so far
    
    # initialization method 
    def __init__ (self, x = 0, y = 0): #default arguments technique
        self.__x = x
        self.__y = y
        Point.__count += 1  #update the Point count, each time we create a new Point
    
    # getters
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def printPoint(self):
        return '(' + str(self.__x) + ', ' + str(self.__y) + ')'
    
    # setters
    def setPoint(self, x, y):
        self.__x = x
        self.__y = y
    
    def reset(self):
        self.setPoint(0, 0)
        
    # other methods
    def distance(self, p):
        return math.sqrt( (self.getX() - p.getX()) ** 2 + (self.getY() - p.getY()) ** 2)
    
    # static methods
    @staticmethod
    def printPointCount():
        print("Points created:", Point.__count)
        
    @staticmethod
    def getPointCount():
       return Point.__count

#the following code will execute only if this file is not being used as a module
if __name__ == "__main__" :
    # create some point objects
    p1 = Point()
    p2 = Point(10, 10)
    
    # print the points
    print('We have created', Point.getPointCount(), 'points:')
    print('p1 =', p1.printPoint())
    print('p2 =', p2.printPoint())
    
    # calculate the distance between p1 and p2
    dist = p1.distance(p2)
    print('The distance between p1 and p2 is', round(dist, 2))

        
