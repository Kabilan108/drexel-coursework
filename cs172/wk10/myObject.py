#File:     myObject.py
#Purpose:  Simple class MyObject to demostrate the hash method
#Author:   Adelaida A. Medlock
#Date:     March 2, 2021

class MyObject():
    def __init__(self, value):
        self.__value = value
    
    def getValue(self):
        return self.__value
        
    def __hash__(self):
        return ord(self.__value) - 32
    
    def __str__(self):
        return ('Value of my object: ' + str(self.__value))


# main script to test MyObject class
if __name__ == "__main__":
    sampleObj = MyObject('?')
    secondSample = MyObject('p')
    print(sampleObj)
    print('Hash value for my object is:', hash(sampleObj))
    print(secondSample)
    print('Hash value for my object is:', hash(secondSample))
    