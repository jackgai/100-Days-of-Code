from tkinter import *


def miles_to_km():
    mile = float(entry.get())
    km = round(1.609 * mile)
    label_res.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

# labels
label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_res = Label(text="0")
label_res.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

# entry
entry = Entry(width=10)
entry.grid(column=1, row=0)

# button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
