#Program:     Sorting_Part1.py
#Purpose:     Demo selection and insert sort
#Author:      Adelaida Medlock
#Date:        December 1, 2020

'''
    swap():        exchanges the values of two elements in a list
    Parameters:    a list of values, the indeces of the elements to be swapped
    Return value:  none
    Example:       swap (myList, 3 ,5)
'''
def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

'''
    selection_sort(): implements the selection sort algorithm
                      This implementation sorts in ascending order
    Parameters:       a list of items to be sorted
    Example:          selection_sort(myList)
'''
def selection_sort(values):
    for i in range(len(values) - 1):
        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(values)):
            if values[j] < values[index_smallest]:
                index_smallest = j
    
        # Swap values[i] and values[index_smallest]
        swap(values, i, index_smallest)

def selection_sort_descend(values):
    for i in range(len(values) - 1):
        # Find index of largest remaining element
        index_largest = i
        for j in range(i + 1, len(values)):
            if values[j] > values[index_largest]:
                index_largest = j
    
        # Swap values[i] and values[index_smallest]
        swap(values, i, index_largest)
        

'''
    insertion_sort(): implements the insertion sort algorithm
                      This implementation sorts in ascending order
    Parameters:       a list of items to be sorted
    Example:          insertion_sort(myList)
'''
def insertion_sort(values):
    for i in range(1, len(values)):
        j = i
        # Insert values[i] into sorted part 
        # stopping once values[i] in correct position
        while j > 0 and values[j] < values[j - 1]:
            # Swap values[j] and values[j - 1]
            swap(values, j, j - 1)
            j = j - 1

def insertion_sort_descend(values):
    for i in range(1, len(values)):
        j = i
        # Insert values[i] into sorted part 
        # stopping once values[i] in correct position
        while j > 0 and values[j] > values[j - 1]:
            # Swap values[j] and values[j - 1]
            swap(values, j, j - 1)
            j = j - 1


#driver
if __name__ == "__main__" :
    #testing selection sort
    list1 =  [1, 33, 98, 45, 2, 11, -3, 0, 41]
    
    print('Testing selection sort')
    print('Unsorted list:')
    print(list1)
    print()
    selection_sort(list1)
    print('Sorted list:')
    print(list1)
    print()
    
    #testing insertion sort
    print()
    list2 = ['ann', 'tim', 'jim', 'sue', 'kat', 'bob']
    print('Testing insertion sort')
    print('Unsorted list:')
    print(list2)
    print()
    insertion_sort(list2)
    print('Sorted list:')
    print(list2)
    print()
    
