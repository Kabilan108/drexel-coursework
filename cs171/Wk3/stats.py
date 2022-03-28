#File Name: stats.py
#Purpose:   This program asks the user to enter quiz grades
#           and then calculates basic stats
#Author:    Adelaida A. Medlock
#Date:      10/5/20

#intro
print('This program asks the user to enter quiz grades and then calculates basic stats')

#ask use how many values they want to enter
howMany = int(input('How many quiz grades do you need to enter? '))

#read values from keyboard and store them in a list
quizzes = [float(input("Enter Quiz %d Grade: " %(x + 1))) for x in range (0, howMany)]

#calulate basic stats on the values
total = sum(quizzes)
average = total / len(quizzes)
high = max(quizzes)
low = min(quizzes)

#display formatted output
print()
print('%-8s %8d' %('Values:', howMany ))
print('%-8s %8.2f' %('Total:', total))
print('%-8s %8.2f' %('Highest:', high))
print('%-8s %8.2f' %('Lowest:', low))
print('%-8s %8.2f' %('Average:', average))
