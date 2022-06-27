"""
Sorting Algorithms
Here, I'll be implementing different sorting algorithms.
"""

import rich
import random

def swap(values, i, j):
    """Swap values in a list"""
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

def selection_sort(values):
    """Implementation of the Selection Sorting Algorithm
    This sorts a lis in ascending order by locating the smalest value,
    switching it with the first value, and repeating this proces, moving
    through the list from left to right.
    """

    for i in range(len(values) - 1):  # last value will already be sorted so -1
        # Find index of minimum value
        minimum_ind = i
        for j in range(i + 1, len(values)): # Loop through following positions
            if values[j] < values[minimum_ind]:
                minimum_ind = j

        # swap values[i] and values[minimum_ind]
        swap(values, i, minimum_ind)

def insertion_sort(values):
    """Implementation of the Insertion Sorting Algorithm
    - Consider the first item to be a sorted sub-list (of one item)
    - Insert the second element, by exchanging if necessary
        - The first and second element are in the proper place
    - Insert the 3rd element in the appropriate position relative to the first two
    - Insert the 4th element in the appropriate position relative to the first three
    - and so on ...
    """
    for i in range(1, len(values)): # loop through the list (excluding 1st)
        j = i
        # insert values[i] into sorted part
        # stopping once values[i] in corrected position
        while j > 0 and values[j] < values[j - 1]:
            # swap values[j] and values[j-1]
            swap(values, j, j-1)
            j -= 1

def merge_sort(values):
    """Implementation of the Merge Sort Algorithm
    - Start with an unordered list of elements
    - Repeatedly break this list into roughly equal parts
    - Countinue until each part consists of only a single element
        - A single element is sorted
    - Merge each sorted part (starting from single elements)
        - Put each element in the proper position
    """


def tests():

    rich.print("[magenta bold]Testing Sorting Algorithms[/magenta bold]")

    # Create list for testing, and sort it with pythons default method
    L = [random.randint(0, 100) for _ in range(10)]
    sorted_L = L.copy()
    sorted_L.sort()

    # Selection Sort
    selection_sorted = L.copy()
    selection_sort(selection_sorted)
    # Insertion sort
    insertion_sorted = L.copy()
    insertion_sort(insertion_sorted)

    # Print results
    rich.print("[red] Original List:[/red]  ", L, end='')
    rich.print("[red]  Default Sort:[/red]  ", sorted_L, end='')
    rich.print("[red]Selection Sort:[/red]  ", selection_sorted, end='')
    rich.print("[red]Insertion Sort:[/red]  ", insertion_sorted, end='')
    

if __name__ == '__main__':
    tests()