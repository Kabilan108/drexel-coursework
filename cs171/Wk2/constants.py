#Program:            constants.py
#Purpose:            store physics constants needed for various calculations
#Author:             Mark Boady
#Edited & formatted: Adelaida A. Medlock
#Date:               January 13, 2019

# Physics Constants
Gravity = 6.67 * 10 ** (-11)      # in m^2/kg/s^2
EarthMass = 5.97 * 10 ** (24)     # in kg
EarthRadius = 6.378 * 10 ** (6)   # in m

# All below in meters
JupiterRadius = 71.492 * 10 ** (6)
SaturnRadius  = 60.268 * 10 ** (6)
UranusRadius  = 25.559 * 10 ** (6)
NeptuneRadius = 24.764 * 10 **(6)
VenusRadius   = 6.051 * 10 ** (6)
MarsRadius    = 3.396 * 10 ** (6)
MercuryRadius = 2.439 * 10 ** (6)
MoonRadius    = 1.738 * 10 ** (6)
PlutoRadius   = 1.195 * 10 ** (6)

# All Below in kg
MercuryMass = 0.330 * 10 ** (24)
VenusMass   = 4.87 * 10 ** (24)
MoonMass    = 0.073 * 10 ** (24)
MarsMass    = 0.642 * 10 ** (24)
JupiterMass = 1898 * 10 ** (24)
SaturnMass  = 568 * 10 ** (24)
UranusMass  = 86.8 * 10 ** (24)
NeptuneMass = 102 * 10 ** (24)
PlutoMass   = 0.0146 * 10 ** (24)

# Unit Conversion
mps_to_milesph = (3600 * 100) / (5280 * 12 * 2.54)

if __name__ == "__main__":
    print("This file stores Physics Constants.")
    print("Gravity:", Gravity)
    print("EarthMass:", EarthMass)
    print("EarthRadius:", EarthRadius)
    print("m/s to miles/hour:", mps_to_milesph)
