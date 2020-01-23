import tkinter as tk
from tkinter import ttk

from Input import Input

win = tk.Tk()

win.title("Earn Great")

def submit(cc): # commit the data into earning table
    if(cc=="Shoe"):
        sub_mit.submit(shoe_type.get(), earning.get(), location.get(), cc)
    elif(cc=='Shirt'):
        sub_mit.submit(shirt_type.get(), earning.get(), location.get(), cc)
    else:
        print("You need to enter a value!")

#create label frame for the shoe ui
shoe_frame= ttk.Labelframe(win, text ="Shoe Sale")
shoe_frame.grid(column=0, row=0, padx=4, pady=4, sticky='w')
# create combo box for the shoe type
shoe_type = tk.StringVar()
shoe_combo = ttk.Combobox(shoe_frame, width=9, textvariable = shoe_type)
shoe_combo['values']  = ('Baby Girl', 'Baby Boy', 'Boy', 'Girl', 'Man', 'Woman')
shoe_combo.current(0)
shoe_combo.grid(column=0, row=0)
# create the submit button for shoe type
action_shoe = ttk.Button(shoe_frame, text="submit", command= lambda: submit("Shoe"))
action_shoe.grid(column=1, row=0)

#create label frame for the shirt ui
shirt_frame= ttk.Labelframe(win, text ="Shirt Sale")
shirt_frame.grid(column=0, row=1, padx=4, pady=4, sticky='w')
# create combo box for the shirt type
shirt_type = tk.StringVar()
shirt_combo = ttk.Combobox(shirt_frame, width=16, textvariable = shirt_type)
shirt_combo['values']  = ('T-Shirt', 'School Uniform', 'Baby Cloth', 'Jacket', 'Blouse', 'Pajamas')
shirt_combo.current(0)
shirt_combo.grid(column=0, row=0)
# create the submit button for shirt type
action_shirt = ttk.Button(shirt_frame, text="submit", command= lambda: submit("Shirt"))
action_shirt.grid(column=1, row=0)

#create label frame for the earning ui
earning_frame= ttk.Labelframe(win, text ="Earning")
earning_frame.grid(column=1, row=0, padx=4, pady=4, sticky='w')

# create combo box for the shoe earning
earning = tk.StringVar()
earn_combo = ttk.Combobox(earning_frame, width=9, textvariable = earning)
earn_combo['values']  = ('1.00', '2.00', '3.00', '4.00', '5.00', '6.00', '7.00', '8.00', '9.00', '10.00')
earn_combo.current(0)
earn_combo.grid(column=0, row=0)

#create label frame for the location ui
location_frame= ttk.Labelframe(win, text ="Location")
location_frame.grid(column=1, row=1, padx=4, pady=4, sticky='w')

# create combo box for the sale location
location = tk.StringVar()
location_combo = ttk.Combobox(location_frame, width=13, textvariable = location)
location_combo['values']  = ('Down Town', 'Market', 'Bus Station', 'Beach')
location_combo.current(0)
location_combo.grid(column=0, row=0)

win.resizable(0,0)

sub_mit = Input(action_shoe)
sub_mit.setting()

win.mainloop()