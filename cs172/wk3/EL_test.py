#File:     El_test.py
#Purpose:  Testing the EL class and its overloaded operators
#Date:     January 20, 2020
#Author:   Adelaida Medlock

from englishLength import EL

def main():
    print('Testing overaloaded operators for EL')
    print('------------------------------------')
    
    # create some EL objects
    len1 = EL(1,2,3)
    len2 = EL(4,5,6)
    len3 = EL()
    
    # adding len1 and len2 to create len4
    len4 = len1 + len2

    
    # display our EL objects
    print('len1 is', len1)
    print('len2 is', len2)
    print('len3 is', len3)
    print('len4 is', len4)
    print()
    
    # testing the subscript operator
    print('len1[0] is', len1[0])
    print('len1[1] is', len1[1])
    print('len1[2] is', len1[2])
    print('len1[3] is', len1[3])  # this will cause an error
    print()
    
    # testing comparison operators
    if len1 < len2 :
        print('len1 is less than len2')
    else:
        print('len2 is less than len1')
    
    len3.addInches(87)
    print('\nlen3 is', len3)
    
    if len3 == len4 :
        print('\nlen3 and len4 have the same value!')
    else:
        print('\nlen3 and len4 hold different values')