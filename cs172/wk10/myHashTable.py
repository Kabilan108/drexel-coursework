#File:     myHashTable.py
#Purpose:  Demo of hash table implemetation. Instances of MyObject will be used as the key.
#Author:   Adelaida A. Medlock
#Date:     February 23, 2021

from myObject import MyObject

# Create an empty list for our hash table
hashTable = []

# Each element of hashTable is another list
for count in range(0, 95):  # there are 95 printable characters
    hashTable.append([])
    
# show what hash table looks like before populating it
print(hashTable)
    
# Add items to the hash table. Each item is a tuple of the form: (MyObject, integer)
# This hash table uses MyObject as the key and an integer to state
# what place in the input sequence a character was entered
for count in range(1, 6):
    char = input('Enter a single character: ')
    key = MyObject(char)
    index = hash(key)
    hashTable[index].append( (key, str(count) )
    
# iterate the hashtable, find the locations used and print their values
# remember that an element in the table is a tuple
print()
for item in hashTable:
    if len(item) != 0 :
        key = item[0][0].getValue()
        when = item[0][1]
        print(key, 'was entered', when )

# let's see what the hash table looks like
print('\nHere is our hash table:')
for row in hashTable:
    print(row)