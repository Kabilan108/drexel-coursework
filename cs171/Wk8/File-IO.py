#Program:     File-IO.py
#Purpose:     Demo how to open, read, and write from/to files
#Author:      Adelaida Medlock
#Date:        February 21, 2022

import os

'''
replaceWord()
  Purpose: takes a text file in a given directory and replaces all 
           occurrences of originalWord with newWord
  @parameter: directory is a string with the name of the current working directory
  @parameter: filename a string with the name of the data file
  @parameter: orginalWord is a string with the word to be replaced
  @parameter: newWord is a string with the replacement Word
  @return: none
  Example of a call:  replaceWord(r'C:\CS171\', 'myFile.txt', 'old', 'new')
'''
def replaceWord(directory, fileName, originalWord, newWord):
    
    #create path for input file and attempt to open file for reading
    inPath = os.path.join(directory, fileName)
    
    if (os.path.isfile(inPath)) : #file exists
        #open input file for reading
        inFile = open(inPath, 'r')
        
        #creat path for output file and open it for writing
        outFileName = 'out-' + fileName
        outPath = os.path.join(directory, outFileName)
        outFile = open(outPath, 'w')   
        
        #read all the lines in the input file
        lines = inFile.readlines()
        
        #process each line of the input file, and write new line in output file
        for line in lines :
            newLine = line.replace(originalWord, newWord)
            outFile.write(newLine)

        #close both files
        inFile.close()
        outFile.close()
        
    else : #input file does not exist
        print('Error: data file not found')

'''   
fileChecking()
  Purpose: Check that a file exists in a given directory. The function 
           receives the directory, asks the user for the name of a file 
           and it returns a tuple, that has a boolean to indicate whether 
           the file exists in the directory, and the name of the file 
           user entered if it exists.
    
  @parameter: a string with the name of the current working Directory
  @return: a tuple (Bool, fileName) where bool is True if a fileName 
           exists in the directory
  Example of call: aTuple = fileChecking(r'C:\CS171\Examples')
'''
def fileChecking(directory) :
    fileList = os.listdir(directory) 
    fileName = input("Please enter the name of the file you want to open: ")
    if (fileName in fileList) :
        return (True, fileName)
    else :
       return (False, '')


'''
sales()
  Purpose: Read all the values in a data file that contains sales 
           figures (as float values) then calculates the total sales, 
           counts how many values are stored in the file and calculates 
           the average sales. The results are stored in an output file.
  note1: we don't know how many values are in the input file
  note2: we read strings, so to perform calculations on the values read, 
         then we need to convert them  into numbers. To store the results 
         in an output file, we need to convert the numbers into strings    
  @parameter: a string with the name of the current working Directory
  @return: none
  Example of a call:  sales(r'C:\CS171\Examples')
'''
def sales(directory) :
    #getting data file name and checking it exists
    check = fileChecking(directory)
    
    if check[0] :  #file exists, so open and process
        #open data file for reading
        inFile = open(check[1], 'r')  
  
        #read first line from file
        line = inFile.readline() 
        total = 0.0
        count = 0
  
        #Keep processing as long as we don't read an empty string 
        while line != '' :  # '' is an empty string used to indicate the EOF
            #convert line we just read into a floating point number
            amount = float(line) 
            #calculate total
            total = total + amount
            #count how many values we have read so far
            count = count + 1
            #display current value read
            print('Value %d: %.2f' %(count, amount))
            #read the next value
            line = inFile.readline()
    
        #done reading, now close the file
        inFile.close()
  
        #getting ready to store the results in an output file
        print('\nStoring results in results.txt')
        average = total / count
    
        #open ouptut file
        outPath = os.path.join(directory, 'results.txt')
        outFile = open(outPath, 'w')
    
        #we write strings into the file, so the numbers have to be
        #converted to strings before we write them to the file
        outFile.write("Total: " + str(total) + '\n')
        outFile.write("Count: " + str(count) + '\n')
        outFile.write("Average: " + str(average) + '\n')
  
        #done writing, close the file
        outFile.close()
    
    else:  #file does not exist
        print('Error: that file does not exist in this directory')

'''
findPalindromes()
  Purpose: asks the user to enter the name of a file that contains 
           a word per line, then find and displays the palindromes
  @parameter: none
  @return: none
  Example of a call:  findPalindromes()
'''
def findPalindromes() :
    # Open data file that contains 1 word per line
    currentDirectory = os.getcwd()
    file = input('Enter name of the data file: ')
    while file not in os.listdir(currentDirectory) :
        print('Error: that file does not exist. Try again.')
        file = input('Enter name of the data file: ')
    inFile = open(file, 'r')
    
    #parse each line in the file to see if word is a palindrome
    lines = inFile.readlines()
    palindromes = []

    for line in lines:
        #remove trailing spaces
        line = line.rstrip() # rstrip() returns a copy of the string 
                             # with trailing characters removed
    
        #Compare line to it's reverse, if they are equal, append to list
        if line == line[::-1] :
            palindromes.append(line)
	
	# close data file
    inFile.close()
	
    # display results
    print("Found:", len(palindromes), "palindromes:")

    for word in palindromes:
        print(word)
