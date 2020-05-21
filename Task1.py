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
phone_Numbers = set()

for record in texts:
    phone_Numbers.add(record[0])
    phone_Numbers.add(record[1])

for record in calls:
    phone_Numbers.add(record[0])
    phone_Numbers.add(record[1])

print(f"There are {len(phone_Numbers)} different telephone numbers in the records.")