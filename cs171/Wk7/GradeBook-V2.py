#Program:     GradeBook-V2.py
#Purpose:     Simulate a gradebook. Use functions.
#Author:      Adelaida Medlock
#Date:        October 30, 2021

# Define functions needed here
''' Purpose: validates input from the user to be an integer between lower and upper
    Parameters:
       lower:   an integer value representing the minimum acceptable value
       upper: an integer value representing the maximum acceptable value
    Return value: an integer number between lower and upper
    Usage example:  num = int_in_range(10, 20)  
'''  
def int_in_range(lower, upper) :
    stop = False
    while (not stop):
        try:
            print('Enter an integer between', lower, 'and', upper, ':', end = ' ')
            number = int(input())
            while(not(number >= lower and number <= upper)):
                  print('Error: you entered a value out of range. Try again.')
                  print('Enter a value between', lower, 'and', upper, ':', end = ' ')
                  number = int(input())
            stop = True
        except Exception as e:
            print('Invalid input: an integer value was expected. Try again.')
    return number


''' Purpose: Get and validate input from the user
    Parameters: None
    Return value: a list of integer value between 0 and 100
    Usage example:  myList = getData()  
'''  
def getData() :
    stop = False
    scores = []
    while not stop:
        value = int_in_range(0, 100)
        scores.append(value)
        more = input('Do you want to enter another value? (Y/N): ')
        if (more[0].lower() != 'y') :
            stop = True
    
    return scores


''' Purpose: calculate basis stats for a list of scores
    Parameters:
       score:     a list of numeric values
    Return value: a list in the form [count, maximum, minimum, average]
    Usage example:  stats = calculateStats([10, 20, 30])  
'''  
def calculateStats(scores) :
    count = 0
    total = 0
    minimum = 100
    maximum = 0
    
    for score in scores :
        total = total + score
        count = count + 1
        if (score < minimum) :
            minimum = score
        if (score > maximum):
            maximum = score
    
    average = total / count
    return [count, maximum, minimum, average]


''' Purpose: count the number of As, Bs, Cs, Ds, and Fs
    Parameters:
       grades:    a list of numeric values
    Return value: a dictionary in the form {'A':intValue, 'B':inValue, etc}
    Usage example:  letter = countLetters([100, 80, 60])  
''' 
def countLetters(grades):
    letterCount = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0} 
    for index in range(0, len(grades)) :
        if (grades[index] >= 90) :
            letterCount['A'] = letterCount['A'] + 1
        elif (grades[index] >= 80) :
            letterCount['B'] = letterCount['B'] + 1
        elif (grades[index] >= 70) :
            letterCount['C'] = letterCount['C'] + 1        
        elif (grades[index] >= 60) :
            letterCount['D'] = letterCount['D'] + 1
        else :
            letterCount['F'] = letterCount['F'] + 1
    
    return letterCount


''' Purpose: display a report with basic stats on a list of scores
    Parameters:
       stats:       a list that in the form [count, min, max, average]
       letterCount: a dictionary that stores the number of As, Bs, Cs, Ds, Fs
    Return value:   none
    Usage example:  reportResults([5, 10, 1, 5.00], {'A':1, 'B':2})  
'''  
def reportResults(stats, letterCount):
    print('You entered', stats[0], 'grades')
    print('The maximum grade is', stats[1])
    print('The minimum grade is', stats[2])
    print('The average grade is %.2f' %(stats[3]))
    print()
    
    print('Letter Count')
    for letter in letterCount :
        print('%d %s%s'%(letterCount[letter], letter, '(s)'))
    

# the main script
if __name__ == "__main__":
    
    # get and validate input from the user
    grades = getData()
    print()
    
    # perform calculations: basic stats
    stats = calculateStats(grades)

    # count the number of As, Bs, Cs, Ds, and Fs
    letterGrades = countLetters(grades)

    # display results
    reportResults(stats, letterGrades)
    