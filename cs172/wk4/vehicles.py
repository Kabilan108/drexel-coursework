#File Name:  vehicles.py
#Purpose:    Demo for abstract classes
#            Vehicle represents a generic vehicle that runs on fuel
#            Boat and Airplane are derived from Vehicle
#Author:     Adelaida A. Medlock
#Date:       April 14, 2021

from abc import ABC, abstractmethod    # needed to create abstract classes

# Parent Abstrac Class
class Vehicle(ABC):
    # constructor
    def __init__(self, topSpeed, tankVolume, tankCurrent = 0):
        self.__topSpeed = topSpeed
        self.__tankVolume = tankVolume
        self.__tankCurrent = tankCurrent
    
    # getters
    def getTopSpeed(self):
        return self.__topSpeed
    
    def getTankVolume(self):
        return self.__tankVolume
    
    def getTankCurrent(self):
        return self.__tankCurrent
    
    # setters
    def refillTank(self):
        self.__tankCurrent = self.__tankVolume
    
    # abstract methods
    @abstractmethod
    def calcNumMilesOnFullTank(self):   # to be implemented by the derived classes
        pass
    
    @abstractmethod
    def move(self):   # to be implemented by the derived classes
        pass
    
    # overloaded operators
    def __str__(self):
        vStr =  'Top Speed:    ' + str(self.__topSpeed) + ' mph.\n'
        vStr += 'Tank Volume:  ' + str(self.__tankVolume) + ' gallons.\n'
        vStr += 'Current Fuel: ' + str(self.__tankCurrent) + ' gallons.\n'
        return vStr
        
        
# Derived classes    
class Boat(Vehicle):
    
    __milesPerGallon = 4
    
    # constructor
    def __init__(self, topSpeed, tankVolume, hullType, tankCurrent = 0):
        super().__init__(topSpeed, tankVolume, tankCurrent)
        self.__hullType = hullType
        
    # getters
    def getHullType(self):
        return self.__hullType

    # implement the abstract methods
    def calcNumMilesOnFullTank(self):   
        return (super().getTankVolume() * Boat.__milesPerGallon)
    
    def move(self):   
        return "Sailing"
        
    # overloaded operators
    def __str__(self):
        vStr =  super().__str__()
        vStr += 'Hull type:    ' + self.__hullType + '\n'
        vStr += 'Miles on Full Tank: ' + str(self.calcNumMilesOnFullTank()) + ' miles.\n'
        return vStr
    
    
class Airplane(Vehicle):
    
    __milesPerGallon = 0.20
    
    # constructor
    def __init__(self, topSpeed, tankVolume, engineType, tankCurrent = 0):
        super().__init__(topSpeed, tankVolume, tankCurrent)
        self.__engineType = engineType
        
    # getters
    def getEngineType(self):
        return self.__engineType
        
    # implement the abstract methods
    def calcNumMilesOnFullTank(self):   
        return (super().getTankVolume() * Airplane.__milesPerGallon)
    
    def move(self):   
        return "Flying"

    # overloaded operators
    def __str__(self):
        vStr =  super().__str__()
        vStr += 'Engine type:  ' + self.__engineType + '\n'
        vStr += 'Miles on Full Tank: ' + str(self.calcNumMilesOnFullTank()) + ' miles.\n'
        return vStr
    
    
 
if __name__ == "__main__":
    # create some concret objects
    cruiser = Boat(50, 30, 'V-Bottom')
    plane = Airplane(550, 3500, 'Turbojet', 1500)
    
    # print objects
    print('Boat:')
    print(cruiser)
    print('Plane:')
    print(plane)
    
    # refuel
    cruiser.refillTank()
    plane.refillTank()
    
    # check tank
    print('After refueling')
    print('Boat tank level: ', cruiser.getTankCurrent(), 'gallons.')
    print('Plane tank level:', plane.getTankCurrent(), 'gallons.')
    print()
    
    # travel somewhere
    print('We are traveling now')
    print('We are', cruiser.move(), 'in our cruiser boat.')
    print('We are', plane.move(), 'for a vacation on the other side of the pond!')
    