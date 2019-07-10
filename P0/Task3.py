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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
def list_codes(data):
    
    # Bangalore codes and prefixes
	area_code = '080'
	mob_prefix = ['7','8','9']
	tele_mark = '140'

	# Creating list of codes
	list_of_codes = []
    
    # Adding Bangalore to the list
	for i in calls:
		if area_code in i[0]:
			list_of_codes.append(area_code)

		elif i[0][0] in mob_prefix:
			list_of_codes.append(i[0][0:5])

		elif tele_mark in i[0]:
			list_of_codes.append(tele_mark)
    
    # Unique set of codes created
	codes = sorted(set(list_of_codes))

	return '\n'.join(codes)


print("The numbers called by people in Bangalore have codes:")
print(list_codes(calls))


# Part B
def list_num(data):
    
    # Bangalore codes and prefixes
	area_code = '(080)'
	mob_prefix = ['7','8','9']
	tele_mark = '140'

	# Creating list of numbers
	num_calls = len(calls)
	nums = 0

    # Adding Bangalore to the list
	for i in calls:
		if area_code in i[0] and area_code in i[1]:
			nums += 1
    
    # Calculating percentage of '080' numbers
	percentage = (nums/num_calls) * 100
	
	return(round(percentage, 2))

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(list_num(calls)))
