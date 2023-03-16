#File:     person.py
#Purpose:  A hashable class that represents a person
#Author:   Adelaida A. Medlock
#Date:     March 2, 2021

class Person :
    # constructor
    def __init__ (self, name, pid, age = 0):
        self.__name = name
        self.__pid = pid
        self.__age = age
        
    # getters
    def getName(self) :
        return self.__name
        
    def getPID(self) :
        return self.__pid
        
    def getAge(self) :
        return self.__age
    
    # setter for age
    def haveBirthday(self) :
        self.__age += 1
        
    # overloaded operators
    def __str__(self) :
        myStr =  'Name: ' + self.__name + '\n'
        myStr += 'PDI: ' + str(self.__pid) + '\n'
        myStr += 'Age: ' + str(self.__age) 
        return myStr
    
    def __eq__(self, other) :
        n = self.__name == other.getName()
        p = self.__pid == other.getPID()
        a = self.__age == other.getAge()
        return n and p and a
    
    # hash method
    def __hash__ (self) :
        total = 0
        num = self.__pid
        while num > 0 :
            total = total + num % 10
            num = num // 10
        
        return total % 10
            
    