#Program:     Sorting_part2.py
#Purpose:     Demo merge and quick sort
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
    partition():   partitions a list into two parts: one with the high values and one with the low values
    Parameters:    a list of values, index of the 1st element, and the index of the last element
    Example:       splitPoint = partition(myList, 0, len(myList) - 1)
'''
def partition(values, fromIndex, toIndex):
    #  Pick middle element as pivot 
    midpoint = fromIndex + (toIndex - fromIndex) // 2
    pivot = values[midpoint]

    #  Initialize variables
    done = False
    leftIndex = fromIndex
    rightIndex = toIndex
    while not done:
        #  Increment leftIndex while values[leftIndex] < pivot 
        while values[leftIndex] < pivot:
            leftIndex = leftIndex + 1
        
        #  Decrement rightIndex while pivot < values[rightIndex] 
        while pivot < values[rightIndex]:
            rightIndex = rightIndex - 1
        
        # If there are zero or one items remaining, all numbers are partitioned. Return rightIndex 
        if leftIndex >= rightIndex:
            done = True
        else:
            # Swap values[leftIndex] and values[rightIndex],  update leftIndex and rightIndex
            swap(values, leftIndex, rightIndex)
            leftIndex = leftIndex + 1
            rightIndex = rightIndex - 1
    
    return rightIndex


'''
    quick_sort():  Implements the quick sort algorithm, using recursion
                   This implementation sorts in ascending order
    Parameters:    a list of items to be sorted, the indeces of first and last elements to be sorted
    Example:       quick_sort(myList, 0, len(myList) - 1))
'''
def quick_sort(values, fromIndex, toIndex):
    splitPoint = 0
    #Base case: If there are 1 or zero entries to sort, partition is already sorted
    if fromIndex < toIndex:
        # Partition the data within the list. Value splitPoint returned from
        # partitioning is location of last item in low partition
        splitPoint = partition(values, fromIndex, toIndex)
    
        # Recursively sort low partition (fromIndex to splitPoint) and
        # high partition (splitPoint + 1 to toIndex) 
        quick_sort(values, fromIndex, splitPoint)
        quick_sort(values, splitPoint + 1, toIndex)
 
 
'''
    merge():     merges two groups of values in a list: [from, mid] and [mid + 1, to]
    Parameters:  a list of values, index of the 1st element, index of middle element, index of the last element
    Example:     merge(myList, 0, 4, 8)
'''
def merge(values, fromIndex, mid, toIndex):
    merged_size = toIndex - fromIndex + 1    # Size of merged partition
    merged_values = []        # Temporary list for merged values
    for i in range(merged_size):
        merged_values.append(0)
        
    merge_pos = 0      # Position to insert merged number
    
    left_pos = fromIndex   # Initialize left partition position
    right_pos = mid + 1    # Initialize right partition position
    
    # Add smallest element from left or right partition to merged values
    while left_pos <= mid and right_pos <= toIndex:
        if values[left_pos] < values[right_pos]:
            merged_values[merge_pos] = values[left_pos]
            left_pos = left_pos + 1
        else:
            merged_values[merge_pos] = values[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    # If left partition is not empty, add remaining elements to merged values
    while left_pos <= mid:
        merged_values[merge_pos] = values[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    # If right partition is not empty, add remaining elements to merged values
    while right_pos <= toIndex:
        merged_values[merge_pos] = values[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    # Copy merge number back to vlues
    merge_pos = 0
    while merge_pos < merged_size:
        values[fromIndex + merge_pos] = merged_values[merge_pos]
        merge_pos = merge_pos + 1

'''
    merge_sort(): Implements the insertion sort algorithm, using recursion
                  This implementation sorts in ascending order
    Parameters:   a list of items to be sorted, the indeces of first and last elements to be sorted
    Example:      merge_sort(myList, 0, len(myList) - 1)
''' 
def merge_sort(values, fromIndex, toIndex):
    mid = 0
    if fromIndex < toIndex:
        mid = (fromIndex + toIndex) // 2  # Find the midpoint in the partition
        
        # Recursively sort left and right partitions
        merge_sort(values, fromIndex, mid)
        merge_sort(values, mid + 1, toIndex)
        
        # Merge left and right partition in sorted order
        merge(values, fromIndex, mid, toIndex)

#driver
if __name__ == "__main__" :
    # testing merge sort
    list1 = [1, 33, 98, 45, 2, 11, -3, 0, 41]    
    print('Testing merge sort')
    print('Unsorted list:')
    print(list1)
    print()
    merge_sort(list1, 0, len(list1) - 1)
    print('Sorted list:')
    print(list1)
    print()
    print()
    
    # testing quick sort
    list2 = ['ann', 'tim', 'jim', 'sue', 'kat', 'bob']
    print('Testing quick sort')
    print('Unsorted list:')
    print(list2)
    print()
    quick_sort(list2, 0, len(list2) - 1)
    print('Sorted list:')
    print(list2)
    print()
