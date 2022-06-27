#Program:     GradeBook.py
#Purpose:     Demo for, while, nested loops by simulating a gradebook
#Author:      Adelaida Medlock
#Date:        February 2, 2020

#getting and validating input from the user
stop = False
grades = []
while not stop :
    try:
        value = int(input('Enter a grade between 0 and 100: '))
        while not(value >= 0 and value <= 100) :
            print('Error: value out of range. Try again.')
            value = int(input('Enter a grade between 0 and 100: '))
        grades.append(value)
        more = input('Do you want to enter another value? (Y/N): ')
        if (more[0].lower() != 'y') :
            stop = True
            
    except Exception as e :
        print('Invalid input: You need to enter a numeric value')
        
print()

#calculations: maximum, minimum and average grades
count = 0
total = 0
min = 100
max = 0
for grade in grades :
    total = total + grade
    count = count + 1
    if (grade < min) :
        min = grade
    if (grade > max):
        max = grade

average = total / count

#count the number of As, Bs, Cs, Ds, and Fs --using a dictionary
countLetters = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0} 
for index in range(0, len(grades)) :
    if (grades[index] >= 90) :
        countLetters['A'] = countLetters['A'] + 1
    elif (grades[index] >= 80) :
        countLetters['B'] = countLetters['B'] + 1
    elif (grades[index] >= 70) :
        countLetters['C'] = countLetters['C'] + 1        
    elif (grades[index] >= 60) :
        countLetters['D'] = countLetters['D'] + 1
    else :
        countLetters['F'] = countLetters['F'] + 1

#display results
print('You entered', count, 'grades')
print('The maximum grade is', max)
print('The minimum grade is', min)
print('The average grade is', round(average, 2))

for key in countLetters :
    print('There are', countLetters[key], key, '(s)')
    

    

