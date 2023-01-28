#File Name:  main.py
#Purpose:    Test the pets, dog and cat classes
#Author:     Adelaida A. Medlock
#Date:       April 18, 2022

from pets import Pet
from dog import Dog
from cat import Cat

# The showPetInfo function accepts an object
# as an argument, and calls its makeSound method
def showPetInfo(creature):
    if isinstance(creature, Pet):
        print(creature)
        creature.makeSound() #polymorphism in action
    else:
        print('That is not a pet!')

# the main script
if __name__ == "__main__":
    # Create a few Pets
    myPet = Pet('generic pet', 2)
    snoopy = Dog('beagle', 3)
    fluffy = Cat()
    
    pets = [myPet, snoopy, fluffy]
    
    # call the function for all pets in the list
    for pet in pets:
        showPetInfo(pet)  # polymorphism
        print()
    
    # What if we pass a non-pet to the function?
    showPetInfo('a string')

