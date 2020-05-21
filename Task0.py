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
firstRecord = texts[0]
incomingNumber1 = firstRecord[0]
answeringNumber1 = firstRecord[1]
startTimestamp1 = firstRecord[2]

# ---------------------------------------
lastRecord = calls[-1]
incomingNumber2 = lastRecord[0]
answeringNumber2 = lastRecord[1]
startTimestamp2 = lastRecord[2]
length = lastRecord[3]


# print(firstRecord)
print("First record of texts, {0} texts {1} at time {2}".format(incomingNumber1,answeringNumber1,startTimestamp1))


# print(lastRecord)
print("Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(incomingNumber2,answeringNumber2,startTimestamp2,length))
