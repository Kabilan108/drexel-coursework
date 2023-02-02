# CS 172 - Lab 4
#
# Description: Implementation of the Monster and Hero classes.
#
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 02.03.2023

# This class defines a generic Character
# It includes attributes and many implemented methods, in addition to an abstract
# methods __str__ and react
from abc import ABC, abstractmethod

### DO NOT CHANGE ANYTHING BELOW IN THIS Character CLASS ####
class Character(ABC):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage):
        self.__name = name
        self.__health = maxHealth
        self.__description = description
        self.__weaponName = weaponName
        self.__weaponDamage = weaponDamage

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def react(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getWeaponName(self):
        return self.__weaponName
    
    def getWeaponDamage(self):
        return self.__weaponDamage
    
    def attack(self, enemy):
        enemy.takeDamage(self.__weaponDamage)
    
    def takeDamage(self, amount):
        self.__health -= amount
    
    def getHealth(self):
        return self.__health
    
    
## Create a Monster class that inherits from the Character class.
class Monster(Character):
    def __init__(self, name, description, maxHealth , weaponName, weaponDamage, motivation):
        # Initialize parent class with provided information
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)

        # Also create an attribute for motivation (a string)
        self.__motivation = motivation
        
    def __str__(self):
        #Return a string in the form:
        #<name> is a <description>
        #Weapon: <weapon>
        #Current Health: <health>
        #Motivation: <motivation>

        text = (f"{self.getName()} is a {self.getDescription()}\n"
                f"Weapon: {self.getWeaponName()}\n"
                f"Current Health: {self.getHealth()}\n"
                f"Motivation: {self.getMotivation()}")
        return text
    
    def react(self):
        #return a string in the form:
        #<name> laughs maniacally.
        return f"{self.getName()} laughs maniacally."
    
    def getMotivation(self):
        #Return the monster's motivation
        return self.__motivation

## Create a Hero class that inherits from the Character class.
class Hero(Character):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage, defenseName):
        #Initialize parent class with provided information
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)

        #Also creates attributes for defense name (string), and defending status (boolean)
        self.__defenseName = defenseName
        self.__defending = False
        
    def __str__(self):
        #Return a string in the form:  
        #Our hero <name> is a <description>
        #Weapon: <weapon>
        #Defense: <defenseName>
        #Current Health: <health>
        #Defense Status: <isDefending>
        text = (f"Our hero {self.getName()} is a {self.getDescription()}\n"
                f"Weapon: {self.getWeaponName()}\n"
                f"Defense: {self.getDefenseName()}\n"
                f"Current Health: {self.getHealth()}\n"
                f"Defense Status: {self.isDefending()}")
        return text
        
    def react(self):
        #Return a string in the form:
        #<name> charges bravely.
        return f"{self.getName()} charges bravely."
        
    def getDefenseName(self):
        #Return the defense name   
        return self.__defenseName
    
    def isDefending(self):
        #Return the defense status
        return self.__defending
    
    def defend(self):
        #Changes defense status to True
        self.__defending = True
        
    def takeDamage(self, amount):
        #Check defense status
        # If defending, only take 50% damage
        if self.isDefending():
            amount -= amount * 0.5
            self.__defending = False

        # Take the damage by calling the parent class' takeDamage method
        super().takeDamage(amount)

