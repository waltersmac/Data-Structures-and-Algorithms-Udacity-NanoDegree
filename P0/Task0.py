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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Obtaining data from texts.csv
first_text = texts[0][0]
ans_text = texts[0][1]
time_text = texts[0][2].split()[1]

# Obtaining data from calls.csv
last_call = calls[-1][0]
ans_call = calls[-1][1]
time_call = calls[-1][2].split()[1]
dur_call = calls[-1][3]

print("First record of texts, {} texts {} at time {}".format(first_text, ans_text, time_text))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call, ans_call, time_call, dur_call))

