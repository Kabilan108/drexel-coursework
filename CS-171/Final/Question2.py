# CS 171 - Final Question 2 (20.2)
# Purpose: 
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.15.2022

def enigma2022(a):
    if a == 1:
       return 1
    else:
       return a**2 + enigma2022(a - 1)
# Part 1: What does enigma2022(a) do? What what does this function compute?
# The enigma2022() function computes the sum of the squares of all numbers
# from 1 to a recursively

# Part 2: Write a implementation of the function that uses loop(s) to solve the problem
# Your enigma2022Loop function definition goes below this line
def enigma2022Loop(a):
    value = 0
    for n in range(1, a+1):
        value += n**2
    
    return value