"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longest_dur(data):
    
    # Creating a dictionary for number
    # and duration time
    calls_dict = {}
    
    # Adding numbers from number initiating the call
    # and also receiving the call
    for i in data:
    	calls_dict[i[0]] = int(i[3])
    	calls_dict[i[1]] = int(i[3])
    
    num_max = None
    num_dur = 0

    for k,v in calls_dict.items():
    	if v > num_dur:
    		num_dur = v
    		num_max = k

    return [num_max, str(num_dur)]

number, time = longest_dur(calls)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(number, time))

