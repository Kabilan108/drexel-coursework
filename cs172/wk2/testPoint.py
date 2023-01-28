#File Name:   testPoint.py
#Purpose:     Test the point class
#Author:      Adelaida Medlock
#Date:        January 16, 2021

from point import Point

if __name__ == "__main__" :
    # create some point objects
    p1 = Point()
    p2 = Point(13)
    p3 = Point(5, 20)
    
    # print the points
    print('We have created', Point.getPointCount(), 'points:')
    print('p1 =', p1.printPoint())
    print('p2 =', p2.printPoint())
    print('p3 =', p3.printPoint())
    
    # change p1 to coordinates entered by the user
    x = int(input('Enter new x-coordinate for p1: '))
    y = int(input('Enter new y-coordinate for p1: '))
    p1.setPoint(x, y)
    
    # calculate the distance between p1 and p2
    dist = p1.distance(p2)
    print('The distance between p1 and p2 is', round(dist, 2))
    
    # calculate the distance between p2 and p3
    dist = p2.distance(p3)
    print('The distance between p2 and p3 is', round(dist, 2))