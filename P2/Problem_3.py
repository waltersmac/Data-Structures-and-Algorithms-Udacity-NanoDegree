def mergesort(array):
    if len(array) <= 1:
        return array

    if len(array) % 2 == 0:
        midpoint = (len(array) // 2)
    else:
        midpoint = (len(array)+1) // 2

    left = mergesort(array[:midpoint])
    right = mergesort(array[midpoint:])

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = mergesort(input_list)

    value1 = []
    value2 = []

    for i in range(len(input_list)):
        if i % 2 == 0:
            value1.append(input_list[i])
        else:
            value2.append(input_list[i])

    value1 = int("".join(str(i) for i in value1))
    value2 = int("".join(str(i) for i in value2))
        
    return [value1, value2]
    
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case1 = test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case3 = test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_case2 = test_function([[1, 0], [0,1]])
test_case2 = test_function([[6, 8, 3], [86, 3]])
