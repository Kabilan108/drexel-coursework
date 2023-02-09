#File:      DrawableObjects.py
#Purpose:   Demo of a basic program using pygame
#           Case study for inheritance and Abstract Base classes 
#Author:    A. Medlock
#Date:      February 3, 2021

import pygame
from abc import ABC, abstractmethod

# abstract class to represent a drawable obejct
class Drawable(ABC):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def getLocation(self):
        return (self.__x, self.__y)

    def setLocation(self, point):
        self.__x = point[0]
        self.__y = point[1]

    def moveRight(self):
        self.__x += 1
        
    def moveLeft(self): 
        self.__x -= 1

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def getRectangle(self):
        pass

      
# derived class that represents a House
class House(Drawable):
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color

    def draw(self, surface):
        location = self.getLocation()
        pygame.draw.rect(surface, self.__color, [location[0] - 15, location[1] - 10, 30, 20])
        pygame.draw.polygon(surface, self.__color, [(location[0] - 15, location[1] - 10), (location[0] + 15, location[1] - 10), (location[0], location[1] - 20)])

    def getRectangle(self):
        location = self.__getLocation()
        return pygame.Rect( [location[0] - 15, location[1] - 20, 30, 30] )
      
# derived class that represents a Snowman
class Snowman(Drawable):
    def __init__(self, x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color    
    
    def draw(self,surface):
        location = self.getLocation()
        pygame.draw.circle(surface, self.__color, [location[0], location[1]], 20)
        pygame.draw.circle(surface, self.__color, [location[0], location[1] - 20], 15)
        pygame.draw.circle(surface, self.__color, [location[0], location[1] - 40], 10)

    def getRectangle(self):
        location = self.__getLocation()
        return pygame.Rect( [location[0] - 20, location[1] - 45, 40, 90] )
    
# derived class for Text
class Text(Drawable):
    def __init__(self, message = "Pygame", x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        fontObj = pygame.font.Font("freesansbold.ttf", 26)
        self.__surface = fontObj.render(message, True, color)
    
    def draw(self, surface):
        surface.blit(self.__surface, self.getLocation())

    def getRectangle(self):
        return self.__surface.get_rect()

# derived class for ground
class Ground(Drawable):
    def __init__(self, x = 0, y = 0, w = 0, h = 0, color = (0,0,0)):
        super().__init__(x, y)
        self.__color = color
        self.__width = w
        self.__height = h
    
    def draw(self, surface):
        location = self.getLocation()
        pygame.draw.rect(surface, self.__color, [location[0], location[1], self.__width, self.__height])

    def getRectangle(self):
        return pygame.Rect( [location[0], location[1], self.__width, self.__height] )


# a collision detection funcion
def collisionDetection(rect1, rect2) :
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y) :
        return True
    return False

# main scrip starts here
if __name__ == "__main__":
    #initialization                           
    pygame.init()
    surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('My Drawable Objects')
    
    # add clock for refreshing screen
    fpsclock = pygame.time.Clock()

    # list of drawable objects to be displayed
    drawables = []                 
    newHouse = House(100, 200, (255, 0, 0))
    drawables.append(newHouse)
    newSnow = Snowman(200, 200, (255, 255, 255))
    drawables.append(newSnow)
    newText = Text('Python and Pygame!', 75, 50, (0, 0, 255))
    drawables.append(newText)
    ground = Ground(0, 210, 400, 300, (255, 255, 255))
    drawables.append(ground)

    # game loop
    while True: 
        for event in pygame.event.get():  #get and process events
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
        
        #clear surface wit color
        surface.fill((204, 229, 255))
        
        # get each drawable obj and draw it
        for drawable in drawables:
            drawable.draw(surface)

        #animation #1
#        surface.fill((204, 229, 255))
#        for drawable in drawables:
#            drawable.moveRight()
#            drawable.draw(surface)
#
        #animation #2
        surface.fill((204, 229, 255))
        for drawable in drawables:
            newSnow.moveRight()
            drawable.draw(surface)

        #update display
        pygame.display.update()
        fpsclock.tick(15)


