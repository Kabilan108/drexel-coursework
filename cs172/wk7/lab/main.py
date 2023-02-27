# CS 172 - Lab 6
#
# Description: Main script for postfix and stack
#      Author: Tony Kabilan Okeke <tko35@drexel.edu>
#        Date: 02.23.2023

from stackclass import Stack

# List of mathematical operators
operators = ['+', '-', '*', '/']


def postfix(exp: str):
    """
    Postfix expression evaluator.

    Parameters
    ----------
    exp : str
        The postfix expression to evaluate.

    Returns
    -------
    int
        The result of the postfix expression.
    """

    compute = Stack()

    for operand in exp.split(' '):
        if operand not in operators:
            compute.push(operand)
        else:
            left, right = compute.pop(), compute.pop()
            result = float(eval(f'{right} {operand} {left}'))
            compute.push(result)

    return compute.pop()


if __name__ == '__main__':
    # Welcome message
    print("Welcome to Postfix Calculator\nEnter exit to quit")

    # Loop until user enters exit
    while True:
        exp = input("Enter Expression\n")

        if exp == 'exit':
            break

        print(f"Result: {postfix(exp)}")

