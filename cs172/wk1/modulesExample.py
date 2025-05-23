#Program:     modulesExample.py
#Purpose:     Demo the usage of random and datetime modules
#Author:      Adelaida Medlock
#Date:        March 28, 2022

# The random module supplies functions to generate pseudo-random values
# randint(a, b) returns a random integer N such that a <= N <= b

import random
def guessGame():
    computer = random.randint(1, 10)
    print ('I have a number between 1 and 10. Try to guess it.')
    count = 1
    
    player = int(input('Enter an number between 1 and 10: '))
    while player != computer :
        count = count + 1
        if player < computer :
            print('Too low. Try again.')
        else :
            print('Too high. Try again.')
        player = int(input('Enter an number between 1 and 10: '))
        
    print ('Good job! It took you', count, 'attempts to guess my number.')
            


# The datetime module supplies classes for manipulating dates and times
# date(year, month, day) creates a date object
# weekday() method of the date class returns the day of the week as an integer, 
#           where Monday is 0 and Sunday is 6

import datetime
def birthday():
    print ("Let's find out what day of the week you were born")
    bday = input('Please enter your birthday in the format mm/dd/yyyy:  ')
    month = int(bday[0:2])
    day = int(bday[3:5])
    year = int(bday[6:])
  
    birthDate = datetime.date(year, month, day)
    dayOfWeek = birthDate.weekday()
  
    print ('You entered:', bday)
    if dayOfWeek == 0 : #Monday
        print ('You were born on a Monday.')
    elif dayOfWeek == 1 : #Tuesday
        print ('You were born on a Tuesday.')
    elif dayOfWeek == 2 : #Wednesday
        print ('You were born on a Wednesday.')
    elif dayOfWeek == 3 : #Thursday
        print ('You were born on a Thursday.')
    elif dayOfWeek == 4 : #Friday
        print ('You were born on a Friday.')
    elif dayOfWeek == 5 : #Saturday
        print ('You were born on a Saturday.')
    else :  #Sunday
        print ('You were born on a Sunday.')