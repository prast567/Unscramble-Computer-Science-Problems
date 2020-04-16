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
from collections import deque, defaultdict

calls_time_add = defaultdict(int)

for call in calls:
    calling, receiving, time, seconds = call
    month = time[3:5]
    year = time[6:10]
    if month == '09' and year == '2016':
         calls_time_add[calling] += int(seconds)
         calls_time_add[receiving] += int(seconds)

max_pnoneNum = max(calls_time_add, key=calls_time_add.get)

print("%s spent the longest time, %s seconds, on the phone during September 2016."%(max_pnoneNum,calls_time_add[max_pnoneNum]))





