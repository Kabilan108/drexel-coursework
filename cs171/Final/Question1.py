# CS 171 - Final Question 1 (20.1)
# Purpose: Compute the hodge psi function
# Author:  Tony Kabilan Okeke (tko35)
# Date:    03.15.2022


# Function definitions
def h_psi(a, n):
    """"
    This function computes to sum of fractions n^k / k^a given a and n
    for k values from 1 to n.
    @params a, n
        Parameters for the Hodge Psi Function
    @return
        value of Hodge Psi
    """
    return sum([n**k / k**a for k in range(1, n+1)])