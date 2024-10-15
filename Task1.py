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
tel_num = set()

for i in range(len(texts)):
    tel_num.add(texts[i][0])
    tel_num.add(texts[i][1])

for i in range(len(calls)):
    tel_num.add(calls[i][0])
    tel_num.add(calls[i][1])


print("There are %s different telephone numbers in the records."%len(tel_num))


## Solution 2
unique_numbers = set()

for text in texts:
    unique_numbers.update([text[0], text[1]])
for call in calls:
    unique_numbers.update([call[0], call[1]])

print('There are {} different telephone numbers in the records.'.format(len(unique_numbers)))
