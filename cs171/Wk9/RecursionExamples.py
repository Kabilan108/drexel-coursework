#Program:     RecursionExamples.py
#Purpose:     Demo how to write and trace recursive functions
#Author:      Adelaida Medlock
#Date:        November 10, 2020

import random  #to be able to generate random numbers


'''
    sumOfDigits(): calculates and returns the sum of all the digits in an integer number
    Parameter:     an integer number
    Return value:  an integer number that stores the sum of the digits in the parameter
    Example of usage:  total = sumOfDigits(12456)
'''
def sumOfDigits(number) : 
    if  number < 0 :   #take care of negative numbers
        return (-sumOfDigits( -number ) )
    if number < 10 :  #base case: a single digit number
        return number
    else:
        #recursive call: Add the last digit to the result of summing the remaining digits
        return ( number % 10 + sumOfDigits( number // 10 ) )  

'''
    fibonacci():   calculates and returns the nth number in the Fibonacci series, where
                   Fibonacci series: 0 1 1 2 3 5 8 13
    Parameter:     an integer number that represents the number in the sequence we want to obtain
    Return value:  an integer that represents the nth number in the Fibonacci series
    Example of usage:  value = fibonacci(2)
'''
def fibonacci(number) :
    if number == 1 :      #base case
        return 0
    elif number == 2  :   #base case
        return 1
    else: #recursive calls
        return ( fibonacci(number - 1) + fibonacci(number - 2))  

'''
    factorial():   calculates and returns the factorial of a number
    Parameter:     a positive integer number
    Return value:  the result of 1 * 2 * 3 * 4 * ..... * number
    Example of usage:  result = factorial(2)
'''
def factorial (number) :
    if (number == 0):  # Base case
        return 1 
    else :  # Recursive call
        return (number * factorial(number - 1) )

'''
    factorial_V2():  calculates and returns the factorial of a number
                     this version uses tail recursion
    Parameters:      a positive integer number to calculate the factorial of
                     optional parameter: an integer to store the result
    Return value:    the result of 1 * 2 * 3 * 4 * ..... * number
    Example of usage:  result = factorial_V2(2)
'''    
def factorial_V2(number, result = 1) :
    if (number == 0):  # Base case
        return result
    else :  # Recursive call
        return factorial_V2(number - 1, result * number)
    

'''
    print_message(): displays a given message a certain number of times
    Parameters:      an integer number that represents the number the number of times to display the message
                     a string that represents the message to be displayed 
    Return value:    none
    Example of usage:  print_message(5, 'Python is fun!')
'''
def print_message(times, message):
    if times > 0:
        print(message)
        print_message(times - 1, message)   # Recursive call
    else :
        print('Done!')  #base case

'''
    rangeSum():      calculates and returns the sum of a specified range of items in a numeric list
    Parameters:      numbers: a numeric list
                     start: the index of the starting item
                     end: the index of the ending item
    Return value:    the total of adding al values between start and end (inclusive)
    Example of usage:  total = rangeSum(numList, 5, 10)
'''
def rangeSum(numList, start, end):
    if start > end :
        return 0
    else :
        return numList[start] + rangeSum(numList, start + 1, end)

'''
    another version that takes advantage of slicing
'''
def rangeSum2(numList):
    if len(numList) < 1 :
        return 0
    else :
        return numList[0] + rangeSum2(numList[1:])

'''
    down_up_word(word): displays a string in a interesting shape
    Parameter:          a string that represents the message to be displayed 
    Return value:       none
    Example of usage:  down_up_word('Python')
    Output: Python
            ython
            thon
            hon
            on
            n
            on
            hon
            thon
            ython
            Python
'''
def down_up_word(word) :
    print (word)
    if len(word) != 1 :  #the base case is when len(word) == 1
        down_up_word(word[1:]) #recursive case
        print(word)

#main function: test the recursive functions
def main():
    print('Testing the sumOfDigits() function')
    n = int(input('Enter an integer value: '))
    sum = sumOfDigits(n)
    print('The sum of the digits in', n, 'is', sum)
    print()
    
    print('Testing the fibonacci() function')
    n = int(input('Enter what number in the fibonacci sequence you want to see: '))
    value = fibonacci(n)
    print('The', n, 'th value in the Fibonacci sequence is',  value)
    print()        
    
    print('Testing the factorial() function')
    n = int(input('Enter what number for which you wish to see the factorial: '))
    result = factorial(n)
    print('The factorial of', n, 'is',  result)
    print()
    
    print('Testing the factorial_V2() function - tail recursion version')
    result = factorial_V2(n)
    print('The factorial of', n, 'is',  result)
    print()
    
    print('Here is a message')
    print_message(5, 'Python is fun!')
    print()
    
    print('Testing sumRange()')
    numbers = [random.randint(1, 100) for x in range(1, 11)]
    total = rangeSum(numbers, 0, len(numbers) - 1)
    print('total =', total)
    print()
    
    print('Testing sumRange2()')
    total2 = rangeSum2(numbers)
    print('total2 =', total2)
    print()
    
    print('Testing down_up_word() function')
    down_up_word('Python')
    print()

    