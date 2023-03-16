#File:     main.py
#Purpose:  Demo of hash table implemetation.
#          Instances of Person will be used as the key.
#          A department will be associate with each key
#          as the pair (Person, department)
#Author:   Adelaida A. Medlock
#Date:     March 2, 2021

from person import Person
from random import randint

# this function calculate the hash value of an person ID (pid)
# using the same algorithm as in the Person class
def calculateHashValue(value) :
    total = 0
    while value > 0 :
        total = total + value % 10
        value = value // 10
    return total % 10

# this function searches the hash table for a given value
def search(table, value) :
    for index in range (len(table)) :
        if table[index][0].getPID() == value :
            return index
    return -1

# the main routine
if __name__ == "__main__" :
    
    # create an empty list to house the hash table
    hashTable = []

    # Each element of hashTable is another list - there are only 10 rows in the table
    # because our hash function returns values between 0 and 9
    for count in range(0, 10):
        hashTable.append([])
    
    # Add items to hash table. Each item is a tuple in the form: (Person, department)
    # we will be using Person objects as the key and department will be
    # a string representing the deptment where person works
    for count in range(1, 5) :
        name = input('Enter the name of the employee: ')
        age =  input('Enter the age of the employee: ')
        eid = randint(100, 999)
        key = Person(name, eid, age)
        index = hash(key)
        dept = input ("Enter the employee's department: ")
        hashTable[index].append( (key, dept) )
        print()
    

    # iterate over hash table, find locations that have values stored and print then
    # remember that each element in the table is a tuple
    print()
    for row in hashTable :
        if len(row) != 0:
            for pair in row :
                key = pair[0]
                dept = pair[1]
                print(key)
                print('Department:', dept)
                print()


    # search for an item in the hash table
    # if found print the key and value associated with it
    # if not found print message
    eid = int(input('Enter EID of item to search for: '))
    index = calculateHashValue(eid)
    location = search(hashTable[index], eid)
    if location != -1 :
        print('Person with ID', eid,  'was located')
        pair = hashTable[index][location]
        print(pair[0])
        print('Department:', pair[1])
    else :
        print('Person with ID', eid,  'was not found in our hash table')

    # print the entire hash table -- this is only so we can see
    # what the entire hash table looks like
    #for row in hashTable :
    #    print(row)
            
