# CS 172 - Midterm Question 2 (Zybooks 15.3)
# Purpose: Implementation of dunder methods for the power class
# Author:  Tony Kabilan Okeke (tko35)
# Date:    02.13.2023


# The Power class
class Power: 
    def __init__(self, base, exponent):
        self.__base = base
        self.__exponent = exponent
        
    def getBase(self):  
        return self.__base
    
    def getExponent(self): 
        return self.__exponent
    
    def setBase(self, base):
        self.__base = base
        
    def setExponent(self, exponent):
        self.__exponent = exponent
    

    # TO-DO: implement the overloaded operators
    def __str__(self): 
        return f"{self.getBase()}^{self.getExponent()}"
    
    def __eq__(self, other): 
        return self.getBase()**self.getExponent() == other.getBase()**other.getExponent()
    
    def __mul__(self, other):
        if self.getBase() == other.getBase():
            return Power(self.getBase(), self.getExponent() + other.getExponent())
        else:
            raise Exception('Invalid bases')
    
    def __pow__(self, exp):
        return Power(self.getBase(), self.getExponent()*exp)
    
    def __getitem__(self, index):
        if index == 0:
            return self.getBase()
        elif index == 1:
            return self.getExponent()
        else:
            raise IndexError('Index must be 0 or 1')
    
# sample main script to check your methods
if __name__ == "__main__":
    p1 = Power(2, 3)
    p2 = Power(2, 5)
    p3 = Power(4, 2)
    print(p1)
    print(p2)
    print(p3)
    
    if (p1 == p2) :
        print(p1, 'and', p2, 'hold the same values')
    else :
        print(p1, 'and', p2, 'hold different values')
    
    p4 = p1 * p2
    print(p4)
    
    try :
        p4 = p1 * p3
    except Exception as e:
        print('Cannot multiply', p1, 'and', p3, ':', str(e) )
        
    p5 = (p3) ** 2
    print(p5)
    
    print('p1 base:', p1[0])
    print('p1 exponent:', p1[1])