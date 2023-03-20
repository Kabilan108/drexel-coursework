# CS 172 - Final Exam
# Purpose: Create the `SolidSet` class
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.20.2023


class SolidSet:
    """Class to store a collection of solid shapes"""

    def __init__(self):
        """Class constructor"""
        self.__solids = []

    def getSolids(self):
        """Getter for solids attribute"""
        return self.__solids

    def getSolid(self, ID):
        """Search for a Solid object by its ID"""
        for solid in self.getSolids():
            if solid.getID() == ID:
                return solid
        return None

    def getSpheres(self):
        """Retrieve all Sphere objects"""
        solids = []
        for solid in self.getSolids():
            if solid.getKind() == "Sphere":
                solids.append(solid)
        return solids

    def getCones(self):
        """Retrieve all Cone objects"""
        solids = []
        for solid in self.getSolids():
            if solid.getKind() == "Cone":
                solids.append(solid)
        return solids

    def addSolid(self, solid):
        """Add a new Solid to the SolidSet"""
        self.__solids.append(solid)

    def getTotalVolume(self):
        """Calculate the total volume of Solids in the SolidSet"""
        volume = 0
        for solid in self.getSolids():
            volume += solid.getVolume()
        return volume
