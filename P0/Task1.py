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

# Function for counting unique telephone numbers
def count_nums(text_data, call_data):
    
    # Create list for unique telephone numbers
    nums_list = set()
    
    # Adding numbers from the texts data
    for i in text_data:
    	nums_list.add(i[0])
    	nums_list.add(i[1])
    
    # Adding numbers from the calls data
    for i in call_data:
    	nums_list.add(i[0])
    	nums_list.add(i[1])


    return 	len(nums_list)		
			
print("There are {} different telephone numbers in the records.".format(count_nums(texts,calls)))
