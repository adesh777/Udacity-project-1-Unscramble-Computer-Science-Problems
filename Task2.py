"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from datetime import datetime
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

def get_Calls_ByMonth_Year(phoneCall, month, year):

    times_tamp = phoneCall[2]
    dt = datetime.strptime(times_tamp, '%d-%m-%Y %H:%M:%S')
    if(dt.year == year and dt.month == month):
        return True
    else:
        return False
        
def track_Call_By_Duration(dictionary, phone_Number, call_Duration):
    if(dictionary.get(phone_Number) == None):
        dictionary[phone_Number] = call_Duration
    else:
        dictionary[phone_Number] = int(
            dictionary.get(phone_Number)) + int(call_Duration)
    return dictionary
records = filter(lambda x: get_Calls_ByMonth_Year(x, 9, 2016), calls)

dictionary = {}
for record in records:
    outgoing_Number = record[0]
    recieving_Number = record[1]
    timestamp = record[2]
    call_Duration = record[3]

    dictionary = track_Call_By_Duration(dictionary, outgoing_Number, call_Duration)
    dictionary = track_Call_By_Duration(dictionary, recieving_Number, call_Duration)
phoneMax = max(dictionary.items(), key=lambda x: int(x[1]))




print(f"{phoneMax[0]} spent the longest time, {phoneMax[1]} seconds, on the phone during September 2016.")