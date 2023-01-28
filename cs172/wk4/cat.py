#File Name:  cat.py
#Purpose:    The Cat class represents a cat, which is a kind of a pet
#Author:     Adelaida A. Medlock
#Date:       April 11, 2022

from pets import Pet

class Cat(Pet):
    # constructor
    def __init__(self, age = 0, hair = 'short'):
        super().__init__('cat', age) # calling constructor from parent class
        self.__hair = hair   #additional attribute represents long or short hair
    
    # getters and setters
    def getHair(self):
        return self.__hair
     
    # additional behavior
    def catchMouse(self) :
        print('Here goes the hunter! Good kitty!')
    
    # override makeSound
    def makeSound(self):
        print('Meow')
        
    # override __str__
    def __str__(self):
        myStr = super().__str__() +  ', ' + self.__hair + ' hair.'
        return myStr
    
    # override the __eq__ operator
    def __eq__(self, other) :
        return (self.__hair == other.getHair() and super().__eq__(other))


