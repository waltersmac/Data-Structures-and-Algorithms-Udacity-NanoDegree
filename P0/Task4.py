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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def tele_mark(data):
    
	tele_mark = '140'

	list_of_numbers = []
    
    # Telephone marketing numbers added to list
	for i in calls:

		# Matching the 140 code with the first 
		# 3 digits of each source number
		if tele_mark == i[0][0:3]:
			list_of_numbers.append(i[0])
    
    # Unique set of telephone marketing numbers
	list_of_numbers = sorted(set(list_of_numbers))
    
	return '\n'.join(list_of_numbers)

print("These numbers could be telemarketers: ")
print(tele_mark(calls))

