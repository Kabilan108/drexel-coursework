# CS 172 - Lab 3
#
# Description: Implementation of a fraction class
#
# Author: Mark Boady & Matt Burlick
# Modified By: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.25.2023

class Fraction:
    #Constructor. Puts fracton in simplest form
    def __init__(self, a, b):
        self.__num = a
        self.__den = b
        self.simplify()
        
    #Print Fraction as a String
    def __str__(self):
        if self.__den == 1 :
            return str(self.__num)
        else:
            return str(self.__num) + "/" + str(self.__den)
            
    #Get the Numerator
    def getNum(self):
        return self.__num
        
    #Get the Denominator
    def getDen(self):
        return self.__den
        
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.__num / self.__den
        
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.__num, self.__den)
        self.__num = self.__num // x
        self.__den = self.__den // x
        
    #Find the GCD of a and b
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
    
    #Compare two fraction objects
    def __eq__(self,other):
        return self.getNum() == other.getNum() and self.getDen() == other.getDen()
    
    #Complete these methods in lab
    def __add__(self, other):
        # Overload + for fractions
        num = self.getNum()*other.getDen() + other.getNum()*self.getDen()
        den = self.getDen() * other.getDen()
        return Fraction(num, den)
        
    def __sub__(self, other):
        # Overload - for fractions
        return self + Fraction(-other.getNum(), other.getDen())
        
    def __mul__(self, other):
        # Overload * for fractions
        return Fraction(self.getNum()*other.getNum(), self.getDen()*other.getDen())
        
    def __truediv__(self, other):
        # Overload / for fractions
        return Fraction(self.getNum()*other.getDen(), self.getDen()*other.getNum())
        
    def __pow__(self, exp):
        # Overload ** for fractions
        if exp < 0:
            return Fraction(self.getDen()**exp, self.getNum()**exp)
        elif exp == 0:
            return Fraction(1, 1)
        else:
            return self * self**(exp-1)

