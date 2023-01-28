# CS 172 - Lab 1
#
# Description: Main script for testing Fraction class.
#
# Author: Tony Kabilan Okeke <tko35@drexel.edu>
# Date: 01.25.2023


# Import fraction class
from fraction import Fraction


def H(n):
    # Harmonic series
    Hn = Fraction(1, 1)
    for k in range(2, n+1):
        Hn += Fraction(1, k)
    return Hn
    
def T(n):
    # 'Two' series
    Tn = Fraction(1,2) ** 0
    for k in range(1, n+1):
        Tn += Fraction(1, 2) ** k
    return Tn
    
def Z(n):
    # 'Zero' series
    return Fraction(2,1) - T(n)
    
def R(n,b):
    # Partial Reimann Zeta
    Rn = Fraction(1,1) ** b
    for k in range(2, n+1):
        Rn += Fraction(1, k) ** b
    return Rn
    

# Main script
if __name__ == "__main__":
    # Welcome message
    print('Welcome to Fun with Fractions!')

    # Collect & validate user input
    while True:
        try:
            n = int(input('Enter Number of iterations (integer>0):\n'))
            if n < 0:
                print('Bad Input')
                continue
            break
        except:
            print('Bad Input')
    
    # Calculate series values
    funcs = ['H', 'T', 'Z', 'R']
    values = [H(n), T(n), Z(n), R(n,n)]

    # Print results
    for f, val in zip(funcs, values):
        if f == 'R':
            print(f"{f}({n},{n})={val}")
            print(f"{f}({n},n})~={val.approximate():.8f}")
        else:
            print(f"{f}({n})={val}")
            print(f"{f}({n})~={val.approximate():.8f}")

