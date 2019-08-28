## Explanation 2
The efficiency of the algorith is O(log(n)), this is because within the while loop the array was halved until the target was found.

I decided to use two helper functions, one to find the pivot point of the array and the other for completing a binary search in the
array that was created. An integer was returned shouwing the index or -1 for not finding the target.