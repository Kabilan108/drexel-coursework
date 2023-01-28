#File Name:   coin.py
#Purpose:     Class to simulate a coin
#Author:      Adelaida Medlock
#Date:        January 1, 2020

import random

class Coin:
    # constructor
    def __init__(self, sideup = 'Heads', value = 1):
        self.__sideup = sideup
        self.__value = value
    
    # getters
    def getValue(self) :
        return self.__value
    
    def getSideup(self):
        return self.__sideup
    
    def getDenomination(self):
        if self.__value == 1 :
            denomination = 'penny '
        elif  self.__value == 5 :
            denomination = 'nickel '
        elif self.__value == 10 :
            denomination = 'dime '
        else : # self.__value == 25 
            denomination = 'quarter '
        
        return denomination
    
    # setters
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            
    # Overloaded operators
    def __str__(self):
        denomination = self.getDenomination()
        coinStr = 'A ' + denomination + 'is ' + self.__sideup + ' up.'
        return coinStr

            
