import tkinter as tk
from tkinter import ttk

from Input import Input

win = tk.Tk()

win.title("Earning Input")

def submit():
    if(description.get()!='' and earning.get()!=""):
        sub_mit.submit(description.get(), earning.get())
    else:
        print("You need to enter a value!")

#create label frame for ui
earn= ttk.Labelframe(win, text = "Daily Earning Input")
earn.grid(column=0, row=0, padx=4, pady=4)
# create label for description
dLabel = ttk.Label(earn, text="Description:").grid(column=0, row=0)
# create text box for description
description = tk.StringVar()
descriptionEntry = ttk.Entry(earn, width=13, textvariable=description)
descriptionEntry.grid(column=1, row=0)

# create label for earning
eLabel = ttk.Label(earn, text="Earning:").grid(column=2, row=0)
# create text box for earning
earning = tk.StringVar()
earningEntry = ttk.Entry(earn, width=13, textvariable=earning)
earningEntry.grid(column=3, row=0)
# create the action button
action = ttk.Button(earn, text="submit", command=submit)
action.grid(column=5, row=0)

win.resizable(0,0)

sub_mit = Input(action)
sub_mit.setting()

win.mainloop()