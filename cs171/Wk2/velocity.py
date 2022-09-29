#Program:             velocity_V2.py
#Purpose:             Determine Escape Velocity on Different Planets
#Author:              Mark Boady
#Edited & formatted:  Adelaida A. Medlock
#Date:                January 12, 2020

# import modules need for calcuations
import constants    #contains constanst needed for calculations
import math         #to be able to use square root and round functions

# define function that calculates the escape velocity, based on given formula
def calculateEscapeVelocity(gravity, mass, radius):
    velocity = math.sqrt(2 * gravity * mass / radius)
    return velocity
    
# main script to calculate escape velocity from each planet and our moon 
print("Escape Velocities")
print("-----------------")

# Mercury
vel = calculateEscapeVelocity(constants.Gravity, constants.MercuryMass, constants.MercuryRadius)
mph = vel * constants.mps_to_milesph
print("Mercury:", round(mph, 2), "miles/hour")

# Venus
vel = calculateEscapeVelocity(constants.Gravity, constants.VenusMass, constants.VenusRadius)
mph = vel * constants.mps_to_milesph
print("Venus:", round(mph, 2), "miles/hour")

# Earth
vel = calculateEscapeVelocity(constants.Gravity, constants.EarthMass, constants.EarthRadius)
mph = vel * constants.mps_to_milesph
print("Earth:", round(mph, 2), "miles/hour")

# Moon
vel = calculateEscapeVelocity(constants.Gravity, constants.MoonMass, constants.MoonRadius)
mph = vel * constants.mps_to_milesph
print("Moon:", round(mph, 2), "miles/hour")

# Mars
vel = calculateEscapeVelocity(constants.Gravity, constants.MarsMass, constants.MarsRadius)
mph = vel * constants.mps_to_milesph
print("Mars:", round(mph, 2), "miles/hour")

# Jupiter
vel = calculateEscapeVelocity(constants.Gravity, constants.JupiterMass, constants.JupiterRadius)
mph = vel * constants.mps_to_milesph
print("Jupiter:", round(mph, 2), "miles/hour")

# Saturn
vel = calculateEscapeVelocity(constants.Gravity, constants.SaturnMass, constants.SaturnRadius)
mph = vel * constants.mps_to_milesph
print("Saturn:", round(mph, 2), "miles/hour")

# Uranus
vel = calculateEscapeVelocity(constants.Gravity, constants.UranusMass, constants.UranusRadius)
mph = vel * constants.mps_to_milesph
print("Uranus:", round(mph, 2), "miles/hour")

# Neptune
vel = calculateEscapeVelocity(constants.Gravity, constants.NeptuneMass, constants.NeptuneRadius)
mph = vel * constants.mps_to_milesph
print("Neptune:", round(mph, 2), "miles/hour")

# Pluto
vel = calculateEscapeVelocity(constants.Gravity, constants.PlutoMass, constants.PlutoRadius)
mph = vel * constants.mps_to_milesph
print("Pluto:", round(mph, 2), "miles/hour")
