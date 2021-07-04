

def bubbleSort(arr, size):
    """ optimised Bubble Sort algorithm
    """
    # Loop to access each element of the list
    for i in range (size-1):
        # Variable to check if swapping occurs
        swapped = False
        # loop to compare two adjacent elements of the list
        for j in range(size-i-1):
            # Comparing two adjacent list elements
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        # If no elements were swapped that means the list is sorted now,
        # then break the loop.
        if swapped == False:
            break
# Prints the elements of the list
def printArray(arr):
    for element in arr:
        print(element, end=" ")
    print("")

arr = [16, 12, 15, 13, 19]
# Finding the length of the list
size = len(arr)
# Printing the given unsorted list
print("Unsorted List:")
printArray(arr)
# Calling bubbleSort() function
bubbleSort(arr, size)
# Printing the sorted list
print("Sorted List in Ascending Order:")
printArray(arr)