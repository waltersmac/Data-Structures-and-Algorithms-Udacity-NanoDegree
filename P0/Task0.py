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

import datetime

first_text = texts[0][0]
ans_text = texts[0][1]
time_text = texts[0][2].split()[1]

last_call = calls[-1][0]
ans_call = calls[-1][1]
time_call = calls[-1][2].split()[1]
dur_call = calls[-1][2].split()[1]

def time_secs(my_time):
	time = my_time.split(':')
	time[0] = int(time[0]) * 60 * 60
	time[1] = int(time[1]) * 60
	time[2] = int(time[2])
	seconds = sum(time)

	return seconds


duration = time_secs(dur_call) - time_secs(time_call)
print(time_secs(dur_call))
print(time_secs(time_call))
print(duration)

# secs = datetime.time(dur_call) - datetime.time(time_call)

print("First record of texts, {} texts {} at time {}".format(first_text, ans_text, time_text))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last_call, ans_call, time_call, dur_call))

