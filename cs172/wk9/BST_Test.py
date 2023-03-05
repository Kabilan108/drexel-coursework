#Program:     BST_Test.py
#Purpose:     Usign a Binary Searth Tree (BST)
#Author:      Adelaida Medlock
#Date:        March 3, 2021

from BST_Implementation import BST
from random import randint

def main():
    
    tree = BST() #empty new BST
    
    # insert 30 random values in the list into the BST, one at the time
    # values inserted will be printable characters
    for i in range(0, 30):
        value = randint(32, 126)  # 32 - 126: ASCII code of printable characters
        char = chr(value)         # corresponding character
        print('Inserting: ', char)
        tree.insert(char)
    print()
    
    # print our BST
    print(tree)
    print()
    
    # searching for a value in the BST
    key = input('Enter character to search in the BST: ')
    if tree.search(key) :
        print ( key, 'was found the the BST')
    else :
        print ( key, 'was not found in the BST')
   