# CS 172 - Lab 4
#
# Description: Main script for the Monster Battle game.
#
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 02.02.2023


# import the Monster and Hero classes here
from characters import Monster, Hero

import random

# This function has two Characters fight
# it returns the winner or None on a tie
def monster_battle(h1, m1):
   
    print("Starting Battle Between")
    print(m1.getName() + ": " + m1.getDescription())
    print(h1.getName() + ": " + h1.getDescription())
   
    # Randomly select who goes first
    if random.randint(0,1) == 0:
        attacker, defender = m1, h1
    else:
        attacker, defender = h1, m1
        
    print(attacker.getName() + " goes first.")
    
    #Loop until someone is unconsious (health < 1) or choose to stop
    stop = False
    while( m1.getHealth() > 0 and h1.getHealth() > 0 and not stop ):
        
        #It will be nice for output to record the damage done
        before_health = defender.getHealth()            

        #Check if the attacker is a monster
        if(isinstance(attacker, Monster)):
            #check if defender is defending, if so print out info about the defense
            if(defender.isDefending()):
                print("Our hero is defending with", defender.getDefenseName(), "!")
            
            
            ######TODO######    
            #Have the attacker react.
            print(attacker.react())
            #Have the attacker attack.
            attacker.attack(defender)
            #Call the print_results function with the necessary info.
            print_results(
                attacker, defender, attacker.getWeaponName(), 
                before_health - defender.getHealth()
            )


        else:
            # Ask the user for the next action: attack, defend, or stop.
            action = input('Pick one of these (a)ttack, (d)efend, or sto(p): ')
        
            ######TODO######    
            #Based on the input, either attack, defend, or end loop
            #If they chose to attack, have the attacker react, attack and then
            #call the print_results function with the necessary info.
            if action == 'a':
                print(attacker.react())
                attacker.attack(defender)
                print_results(
                    attacker, defender, attacker.getWeaponName(), 
                    before_health - defender.getHealth()
                )
            elif action == 'd':
                attacker.defend()
            elif action == 'p':
                stop = True
                break
            else:
                print("Invalid input. Please try again.")
                continue

        
        ######TODO######
        #Swap attacker and defender
        attacker, defender = defender, attacker
        

    ######TODO######    
    #Print out and return who won.
    print("\nBattle is over. let's see who has won...")
    if m1.getHealth() <= 0:
        print(h1.getName(), "is victorious!")
        return h1
    elif h1.getHealth() <= 0:
        print(m1.getName(), "is victorious!")
        return m1
    
    
    
#This function prints the status updates
def print_results(attacker, defender, attack, hchange):
    res = attacker.getName() + " used " + attack
    res += " on " + defender.getName() + "\n"
    res += "The attack did " + str(hchange) + " damage."
    print(res)
    print(attacker.getName() + " at " + str(attacker.getHealth()))
    print(defender.getName() + " at " + str(defender.getHealth()))


#----------------------------------------------------
if __name__=="__main__":
    #Every battle should be different, so we need to
    #start the random number generator somewhere "random".
    #With no input Python will set the seed
    random.seed(0)
   
    ######TODO######    
    #Get Monster's name, description, maxHealth, weaponName, weaponDamage, and 
    #motivation from the user here.
    while True:
        try:
            m_name = input("Enter monster's name: ")
            m_desc = input("Enter monster's description: ")
            m_health = int(input("Enter a number for monster's health: "))
            m_weapon = input("Enter monster's weapon name: ")
            m_weapon_damage = float(input("Enter monster's weapon damage (as a number): "))
            m_motivation = input("Enter monster's motivation: ")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            continue
    #Instantiate a Monster using that info. Note that weaponDamage should be a 
    #floating point number.
    myMonster = Monster(m_name, m_desc, m_health, m_weapon, m_weapon_damage, m_motivation)
        
    ######TODO######    
    #Get the Hero's name,description, maxHealth, weaponName, weaponDamage, defenseName 
    #from the user here.
    while True:
        try:
            h_name = input("Enter hero's name: ")
            h_desc = input("Enter the hero's description: ")
            h_health = int(input("Enter a number for the hero's health: "))
            h_weapon = input("Enter hero's weapon name: ")
            h_weapon_damage = float(input("Enter hero's weapon damage (as a number): "))
            h_defense = input("Enter the hero's defense name: ")
            break
        except ValueError:
            print("Invalid input. Please try again.")
            continue
    #Instantiate a Hero using that info. Note that weaponDamage should be a floating 
    #point number.
    myHero = Hero(h_name, h_desc, h_health, h_weapon, h_weapon_damage, h_defense)
    
    winner = monster_battle(myHero, myMonster)

