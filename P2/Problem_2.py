'''
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
'''
def find_pivot(input_list):

    for index in range(1,len(input_list)-1):
        if input_list[index-1] < input_list[index]:
            continue

        return index


def binary_search(array, target):
    lowindex = 0
    highindex = len(array) - 1

    while lowindex <= highindex:

        mid_index = (highindex + lowindex) // 2
        mid_element = array[mid_index]

        if target == mid_element:
            return mid_index

        elif target < mid_element:
            highindex=mid_index-1

        else:
            lowindex = mid_index + 1

    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """

    pivot_index = find_pivot(input_list)

    if number >= input_list[0]:
        return binary_search(input_list[:pivot_index], number)

    else:
        return pivot_index + binary_search(input_list[pivot_index:], number)




# Testing
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

