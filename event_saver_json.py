#! /usr/bin/env python
import datetime
import json

print("""+++++++++++++++++++++++++++++++++++++++++++++++++++
THIS IS THE SMALL PROGRAM TO STORE EVENTS
+++++++++++++++++++++++++++++++++++++++++++++++ """)

events = []
print("If you want to stop adding press ctrl + Z (windows) or ctrl + D (ubuntu)")
n=-1

try:

 while True:
    event = input("Event : ")
    date = input("Date (dd/mm/yy) : ")
    time = input("Time (24hr) : ")
    place = input("Place :")
    #upload = datetime.datetime.now()
    n =+ 1
    data = {
      "event" : event,
      "date" : date,
      "time" : time,
      "place" : place,
      #"upload" : upload 
    }
    events.append(data)
    print("----------------------------------------------------------")
except:
    print("\n Ented \n")
for element in events:
    for key in element:
        print(key, " : ", element[key])
    print("\n----------------------------------------\n")

    j = json.dumps(events, indent=5)
    outputfile = open('output.json', 'w')
    outputfile.write(j)
    outputfile.close()