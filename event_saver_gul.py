'''
Author : Amjad
Date : 20 May 2021
Program : Event saver
'''

from os import close, remove
import tkinter
import datetime
global n = 1
'''to create heading in file'''

file = open("event_saver.txt", "a")
file.write("""\n+++++++++++++++++++++++++++++++++++++++++++++++++++
THIS IS THE SMALL PROGRAM TO STORE EVENTS
+++++++++++++++++++++++++++++++++++++++++++++++ \n""")
file.close()
    
'''function to clear field when click clear button'''

def clr():
    Event.delete(0)
    Date.delete(0)
    Time.delete(0)
    Place.delete(0)
    #TODO: delete the label texted as Updated

'''function to store and write data from text field and also create label texted as Updated'''
def main():
      event = Event.get()
      date = Date.get()
      time = Time.get()
      place = Place.get()
      data = {
      "event" : event,
      "date" : date,
      "time" : time,
      "place" : place
       }
      file = open("event_saver.txt", "a")
      for key in data:
         file.write(f"{str(key)} : {str(data[key])} \n")
      upload = datetime.datetime.now()
      file.write(f"------------------{n}------------------------{upload}\n")
      file.close()
      global message
      message = tkinter.Label(window, text="Updated check event_saver.txt").grid(row=9)
      n =+ 1

window = tkinter.Tk()
window.geometry("400x200")
window.title("EVENT SAVER")
event = tkinter.Label(window, text="Event : ").grid(row=0, column=0)
Event = tkinter.Entry(window)                                                
Event.grid(row=0, column=1)
date = tkinter.Label(window, text="Date : ").grid(row=1, column=0)
Date = tkinter.Entry(window)
Date.grid(row=1, column=1)
time = tkinter.Label(window, text="Time : ").grid(row=2, column=0)
Time = tkinter.Entry(window)
Time.grid(row=2, column=1)
place = tkinter.Label(window, text="Place : ").grid(row=3, column=0)
Place = tkinter.Entry(window)
Place.grid(row=3, column=1)
empty = tkinter.Label(window).grid(row=5)
empty = tkinter.Label(window).grid(row=6)
button = tkinter.Button(window, text="Done", command=main)
button.grid(row=7, column=10)
button_2 = tkinter.Button(window, text="Clear", command=clr)
button_2.grid(row=7, column=12)
empty = tkinter.Label(window).grid(row=8)
empty = tkinter.Label(window).grid(row=9)
window.mainloop()     






