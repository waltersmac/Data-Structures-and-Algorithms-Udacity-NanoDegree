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

def tele_mark(text_data, call_data):

	list_of_numbers = set()

	send_texts = set()
	rec_texts = set()
	incoming_calls = set()
	outgoing_calls = set()

	for i in text_data:
		if i[0] not in send_texts:
			send_texts.add(i[0])

		if i[1] not in rec_texts:
			rec_texts.add(i[1])

	for i in call_data:
		if i[0] not in outgoing_calls:
			outgoing_calls.add(i[0])

		if i[1] not in incoming_calls:
			incoming_calls.add(i[1])

	for i in outgoing_calls:
		if i not in send_texts and i not in rec_texts and i not in incoming_calls:
			list_of_numbers.add(i)

	return '\n'.join(sorted(list_of_numbers))


print("These numbers could be telemarketers: ")
print(tele_mark(texts,calls))
