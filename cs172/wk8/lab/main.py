# CS 172 - Lab 8
#
# Description: Main script
#      Author: Tony Kabilan Okeke <tko35@drexel.edu>
#        Date: 03.02.2023

# Import the Maze and Room classes
from maze import Maze
from room import Room


def play(my_maze):
    #Play a game
    while not my_maze.atExit():
        # Print the current room
        print(my_maze.getCurrent())

        ## TODO: Get direction from user
        direction = input('Enter direction to move north west east south restart\n')

        ## TODO: Based on choice do what was asked.
        if direction.lower() == 'north':
            move = my_maze.moveNorth()
            if not move:  print('Direction invalid, try again.')

        elif direction.lower() == 'south':
            move = my_maze.moveSouth()
            if not move:  print('Direction invalid, try again.')

        elif direction.lower() == 'east':
            move = my_maze.moveEast()
            if not move:  print('Direction invalid, try again.')

        elif direction.lower() == 'west':
            move = my_maze.moveWest()
            if not move:  print('Direction invalid, try again.')

        elif direction.lower() == 'restart':
            my_maze.reset()

        else:
            print('Invalid Entry')

        # Exit the loop if the player is at the exit
        if my_maze.atExit():
            break

    print("You found the exit!")


# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are 
# applied in that order. This means you arrive at the exit when you go east room and 
# then the north room. The description of each room doesn't matter since the 
# correctness will be graded. The ORDER matters. 
# Create the rooms
room1 = Room("Room1")
room2 = Room("Room2")
room3 = Room("Room3")

# Room 2 is east of Room 1
room1.setEast(room2)
room2.setWest(room1)

# Room 3 is north of Room 2
room2.setNorth(room3)
room3.setSouth(room2)

# Create the maze
SIMPLE_MAZE = Maze(room1, room3)


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, 
# west, west, north, east. This means you arrive at the exit when you go west room, 
# then west room again, then west room again, then take north and then finally the 
# final east room. At the end of the movements, atExit should be true when it is 
# called. The description of each room doesn't matter since the correctness will be 
# graded. 
# Create the rooms
room1 = Room("Room1")
room2 = Room("Room2")
room3 = Room("Room3")
room4 = Room("Room4")
room5 = Room("Room5")
room6 = Room("Room6")

# Room 2 is west of Room 1
room1.setWest(room2)
room2.setEast(room1)

# Room 3 is west of Room 2
room2.setWest(room3)
room3.setEast(room2)

# Room 4 is west of Room 3
room3.setWest(room4)
room4.setEast(room3)

# Room 5 is north of Room 4
room4.setNorth(room5)
room5.setSouth(room4)

# Room 6 is east of Room 5
room5.setEast(room6)
room6.setWest(room5)

# Create the maze
INTERMEDIATE_MAZE = Maze(room1, room6)


if __name__=="__main__":
    play(INTERMEDIATE_MAZE)

