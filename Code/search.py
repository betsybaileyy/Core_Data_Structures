#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    if item is not None:
        if item == array[index]:
            return index
    else:
        return linear_search_recursive(array, item, index+1)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)



# implement binary search iteratively here
# once implemented, change binary_search to call binary_search_iterative
# to verify that your iterative implementation passes all tests
def binary_search_iterative(array, item): # assumes list is sorted to search through

    middle_index = len(array)//2

    value = array[middle_index]

    while value is not None:
        if value == item:
            return value
        elif item > value:
            # value += 1
            value = value + 1
        # return value
        elif item < value:
            # value -= 1
            value = value - 1
            # return value




# implement binary search recursively here
# once implemented, change binary_search to call binary_search_recursive
# to verify that your recursive implementation passes all tests
def binary_search_recursive(array, item, left=None, right=None):

    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1
    if right - left <= 0:
        return None

    middle_index = (right + left) // 2
    value = array[middle_index]

    if value == item:
        return middle_index
    elif item > value:
        value += 1
        return binary_search_recursive(array, item, left, middle_index-1)
    elif item < value:
        value -= 1
        return binary_search_recursive(array, item, middle_index+1, right)
