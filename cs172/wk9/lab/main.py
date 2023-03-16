# File Name: main.py
# Purpose:   Main script for Lab8
# Author:    Tony Kabilan Okeke <tko35@drexel.edu>
# Date:      March 9, 2023

from BST import *
import random


def populateList(n, s):
    """
    Return a list of n randomly shuffled integers in the range [0, n).
    """
    random.seed(s)
    lst = list(range(n))
    random.shuffle(lst)
    return lst


def searchLength(lst, n):
    """
    Return the number of elements of lst that were inspected before finding n.
    """

    for i in range(len(lst)):
        if lst[i] == n:
            return i + 1

    return len(lst)


def listToBST(lst):
    """
    Append the elements of lst to an empty BST and return the BST.
    """
    
    bst = BST()
    for i in lst:
        bst.append(i)
    return bst


if __name__ == "__main__":
    # Create empty lists to store the number of comparisons
    ncomp_list = []
    ncomp_bst = []


    # Seach for values in the BST and list
    for n in range(1, 1000, 100):
        sumcountlist = 0
        sumcountbst = 0
        numruns = 0

        for s in range(1,5):
            lst = populateList(n, s)
            bst = listToBST(lst)

            for v in range(n):
                sumcountlist += searchLength(lst, v)
                sumcountbst += bst.searchLength(v)
                numruns += 1

        # Compute average number of comparisons
        ncomp_list.append(sumcountlist / numruns)
        ncomp_bst.append(sumcountbst / numruns)

    # Print the results
    print("Average Search Length for List: ", ncomp_list)
    print("Average Search Length for BST: ", ncomp_bst)

