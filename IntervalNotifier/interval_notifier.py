import time
from playsound import playsound
from tkinter import *

#pip uninstall playsound
#pip install playsound==1.2.2

window = Tk()
window.title("Interval Notifier")
Label(window, text="Interval").grid(column=0,row=0)
interval_entry = Entry(window, width=10)
interval_entry.grid(column=1, row=0)
Label(window, text="sec").grid(column=2,row=0)
Button(window, text="Start",command=lambda: start_function()).grid(column=3,row=0)

def start_function():
    global interval
    interval = interval_entry.get()
    interval = int(interval)
    for i in range(3):
        playsound('tick.mp3')
    window.after(interval*1000, lambda:end_function())

def end_function():
    for i in range(3):
        playsound('tick.mp3')
    window.after(interval*1000, lambda: end_function())

window.mainloop()