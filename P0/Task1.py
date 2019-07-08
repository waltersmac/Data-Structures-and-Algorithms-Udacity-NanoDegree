"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create list for unique telephone numbers
nums_list = []

# Function for counting unique telephone numbers
def count_nums(text_data, call_data):

	# Adding numbers from texts.csv
	for i in text_data:
		for j in i[:-1]:
			if j not in nums_list:
				nums_list.append(j)
    
    # Adding numbers from calls.csv
	for k in call_data:
		for l in k[:-1]:
			if l not in nums_list:
				nums_list.append(l)
    
    # return number of unique telephone numbers
	return len(nums_list)
		

count_all_nums = count_nums(texts, calls)			
			
print("There are {} different telephone numbers in the records.".format(count_all_nums))
