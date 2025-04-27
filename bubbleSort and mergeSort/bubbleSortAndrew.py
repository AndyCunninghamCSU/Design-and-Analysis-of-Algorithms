# Andrew Cunningham
# CSC506 Spring 2025
# Critical Thinking Assignment 3

# implementation of BubbleSort
# Sorted in place, stable, O(n^2) runtime
# does NOT copy the array, make sure the array isn't changed during operation
def bubbleSortAndrew(array):
    last = len(array) - 1 # last element of the array

    # while we haven't iterated through the entire array n times
    while last > 0:
        # iterate from the start to our current largest element
        for start in range(0, last):
            # if the side-by-side elements are out of order, swap them
            if array[start] > array[start + 1]:
                temp = array[start + 1]
                array[start + 1] = array[start]
                array[start] = temp
        # since we went through the entire array we now know that the largest element is in last
        last = last - 1

testArrays = {
    "Empty Array": [],
    "Single Element Array": [1],
    "2 Element Array": [2, 1],
    "Worst-cast longer array": [99, 50, 20, 2, 1],
    "In order except for middle": [1, 2, 3, 99, 5, 6, 7]
}

for testName, array in testArrays.items():
    print(f"Test: {testName}")
    print(f"  Before: {array}")
    bubbleSortAndrew(array)
    print(f"  After: {array}")