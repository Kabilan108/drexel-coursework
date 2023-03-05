# CS 172 - Lab 8
#
# Description: Simple Maze Class
# Modified By: Tony Kabilan Okeke <tko35@drexel.edu>
#      Author: Mark Boady
#        Date: 03.02.2023


class Room:
    #Constructor sets the description
    #And all four doors should be initially set to None
    def __init__(self, descr):
        # Initialize Room (Node)
        self.__descr = descr

        # Initialize doors
        self.__north = None
        self.__south = None
        self.__east = None
        self.__west = None
        
    #Accessors
    #Return the correct values
    def __str__(self):
        # Return a string description of the room
        return self.__descr
    
    def getNorth(self):
        # Return object north of this room
        return self.__north
    
    def getSouth(self):
        # Return object south of this room
        return self.__south
    
    def getEast(self):
        # Return object east of this room
        return self.__east
    
    def getWest(self):
        # Return object west of this room
        return self.__west
        
    #Mutators
    #Update the values
    def setDescription(self, d):
        # Set the description of the room
        self.__descr = d
    
    def setNorth(self, n):
        # Set the north link of the room to n (only accept Room or None)
        if isinstance(n, Room) or n is None:
            self.__north = n
        else:
            raise TypeError("Links must be of type Room or None")
    
    def setSouth(self, s):
        # Set the south link of the room to s (only accept Room or None)
        if isinstance(s, Room) or s is None:
            self.__south = s
        else:
            raise TypeError("Links must be of type Room or None")
    
    def setEast(self, e):
        # Set the east link of the room to e (only accept Room or None)
        if isinstance(e, Room) or e is None:
            self.__east = e
        else:
            raise TypeError("Links must be of type Room or None")
    
    def setWest(self, w):
        # Set the west link of the room to w (only accept Room or None)
        if isinstance(w, Room) or w is None:
            self.__west = w
        else:
            raise TypeError("Links must be of type Room or None")

