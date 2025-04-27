# Andrew Cunningham
# CSC506 Spring 2025
# Critical Thinking Assignment 3

# Implemetion of Merge Sort
# sorted out of place, stable, O(n log n) runtime, O(n^2) spatial complexity

def mergeSortAndrew(array):
    # base case: we have recursed to one element
    if len(array) <= 1:
        return array
    # recurse by splitting the array in half
    else:
        left = mergeSortAndrew(array[0: len(array) // 2])
        right = mergeSortAndrew(array[len(array) // 2 :])

    leftIndex = 0
    rightIndex = 0

    sortedArray = []

    # start by combining the entire left into sorted
    while leftIndex < len(left):
        # we have NOT hit the end of right
        if rightIndex < len(right):
            # see if left is smaller
            # <= ensures stability by always adding in left first
            if left[leftIndex] <= right[rightIndex]: 
                sortedArray.append(left[leftIndex])
                leftIndex += 1
            # right is smaller
            else:
                sortedArray.append(right[rightIndex])
                rightIndex += 1
        # we have hit the end of right, so just append it
        else:
            sortedArray.append(left[leftIndex])
            leftIndex += 1
    
    # add the rest of right if applicable
    # will attempt to slice an empty list if rightIndex is outside the scope of the array
    sortedArray.extend(right[rightIndex:])
    
    return sortedArray

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
    print(f"  After: {mergeSortAndrew(array)}")