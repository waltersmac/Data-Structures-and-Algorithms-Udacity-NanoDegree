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
    
    # fixed line telephones in Bangalore
	tel_bang = '(080)'

	# Creating list of possible calls
	list_of_calls = []
    
    # Adding Bangalore numbers to the list
	for i in calls:

		# Fixed lines
		if i[0].startswith(tel_bang):
			list_of_calls.append(i[1])

		# Mobile prefixes
		if i[0][:5] == tel_bang and i[1][0] == '7':
			list_of_calls.append([i[0],i[1]])
		if i[0][:5] == tel_bang and i[1][0] == '8':
			list_of_calls.append([i[0],i[1]])
		if i[0][:5] == tel_bang and i[1][0] == '9':
			list_of_calls.append([i[0],i[1]])

		# Tele Marketing
		if i[0][:5] == tel_bang and i[1][0:3] == '140':
			list_of_calls.append([i[0],i[1]])
    
    # Creating set for the codes
	area_codes = set()
    
    # Adding the codes
	for i in list_of_calls:

        # Fixed lines
		if ')' in i:
			p = i.split('(')
			p = p[1].split(')')
			area_codes.add(p[0])

        # Mobile prefixes
		if i[0] in ('7','8', '9'):
			area_codes.add(i[:4])

        # Tele Marketing
		if i[0].startswith('140'):
			area_codes.add(i[:2])

	
	return '\n'.join(sorted(area_codes))


print("The numbers called by people in Bangalore have codes:")
print(list_codes(calls))


# Part B
def list_num(data):
    
    # fixed line telephones in Bangalore
    tel_bang = '(080)'
    
    # Creating list of possibe calls from Bangalore
    poss_calls = []

    # Bangalore fixed line to other Bangalore fixed line calls
    fixed_calls = []


    for i in data:
    	if i[0][:5] == tel_bang:
    		poss_calls.append(i[:2])

    for j in poss_calls:
    	if j[1][:5] == tel_bang:
    		fixed_calls.append(j)
    		

    # Calculating percentage of '080' numbers
    percentage = (len(fixed_calls)/len(poss_calls)) * 100

    return(round(percentage, 2))

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(list_num(calls)))
