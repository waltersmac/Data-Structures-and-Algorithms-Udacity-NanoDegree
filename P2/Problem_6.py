def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    min_num = ints[0]
    max_num = ints[0]

    for value in ints[1:]:

    	if value > max_num:
    		max_num = value

    	elif value < min_num:
    		min_num = value

    	else:
    		continue
    	
    return (min_num,max_num)



## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 11)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((min(l), max(l)) == get_min_max(l)) else "Fail")

print(l)
print(get_min_max(l))