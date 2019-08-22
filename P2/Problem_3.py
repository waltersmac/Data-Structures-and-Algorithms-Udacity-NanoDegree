import copy
import itertools
import math

def combinations(target,data):
    pass


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    max_sum = 0
    max_values = []

    for l in list(itertools.permutations(input_list)):

        if len(l) % 2 == 0:
            midpoint = (len(l)-2) // 2
        else:
            midpoint = (len(l)-1) // 2

    
        value1 = int("".join(str(i) for i in l[:midpoint]))
        value2 = int("".join(str(i) for i in l[midpoint:]))

        value_sum = value1 + value2

        if max_sum <= value_sum:
            max_value2, max_value1  = value2, value1
            max_sum = value_sum
        
    return max_value2, max_value1

    
    



def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]

