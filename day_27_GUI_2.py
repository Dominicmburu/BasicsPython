from tkinter import *

def mile_to_kilometer():
    miles = float(mile_input.get())
    km = round(miles * 1.689, 2)
    total.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
# window.minsize(width=350, height=200)

## mile entry
mile_input = Entry(width=10)
mile_input.insert(END, string="0")
mile_input.grid(column=1, row=0)

# mile label
miles_label = Label(text="Miles", font=("Arial", 18))
miles_label.grid(column=2, row=0)

## label
is_equal = Label(text="is equal to", font=("Arial", 18))
is_equal.grid(column=0, row=1)

# total label
total = Label(text="0", font=("Arial", 18))
total.grid(column=1, row=1)

# km label
km = Label(text="Km", font=("Arial", 18))
km.grid(column=2, row=1)

# calculate button
button = Button(text="Calculate", font=("Arial", 18), command=mile_to_kilometer)
button.grid(column=1, row=2)


window.mainloop()