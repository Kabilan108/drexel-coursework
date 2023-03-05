# CS 172 - Lab 8
#
# Description: Maze Game
# Modified By: Tony Kabilan Okeke <tko35@drexel.edu>
#      Author: Mark Boady
#        Date: 03.02.2023

# Import the Room class
from room import Room


class Maze:
    #Inputs: Pointers to start room and exit room
    #Sets current to be start room
    def __init__(self, st = None, ex = None):
        # Inputs must be either Room or None
        if not (isinstance(st, Room) or st is None):
            raise TypeError("Start must be of type Room or None")
        if not (isinstance(ex, Room) or ex is None):
            raise TypeError("Exit must be of type Room or None")

        #Room the player starts in
        self.__start = st
        
        #If the player finds this room they win
        self.__exit = ex
        
        #What room is the player currently in
        self.__loc = st
        
    #Return the room the player is in (current)
    def getCurrent(self):
        return self.__loc

    #The next four methods all have the same idea
    #See if there is a room in the direction
    #If the direction is None, then it is impossible to go that way
    #in this case return false
    #If the direction is not None, then it is possible to go this way
    #Update current to the new room (move the player)
    #then return true so the main program knows it worked.
    def moveNorth(self):
        if self.getCurrent().getNorth() is not None:
            # Update current location
            self.__loc = self.getCurrent().getNorth()
            print('You went north')

            return True

        return False
    
    def moveSouth(self):
        if self.getCurrent().getSouth() is not None:
            # Update current location
            self.__loc = self.getCurrent().getSouth()
            print('You went south')

            return True

        return False
        
    def moveEast(self):
        if self.getCurrent().getEast() is not None:
            # Update current location
            self.__loc = self.getCurrent().getEast()
            print('You went east')

            return True

        return False
    
    def moveWest(self):
        if self.getCurrent().getWest() is not None:
            # Update current location
            self.__loc = self.getCurrent().getWest()
            print('You went west')

            return True

        return False

    #If the current room is the exit,
    #then the player won! return true
    #otherwise return false
    def atExit(self):
        return self.__loc == self.__exit

    #If you get stuck in the maze, you should be able to go
    #back to the start
    #This sets current to be the start room
    def reset(self):
        self.__loc = self.__start
        print('You went back to the start!')

