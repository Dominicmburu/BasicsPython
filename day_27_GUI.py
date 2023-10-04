## args
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(5,5,4,5))

## kwargs
# def calculate(n, **kwargs):
#     # print(kwargs)
#     # for (key,value) in kwargs.items():
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# calculate(2, add=3, multiply=5) 

# class Car:

#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")

# my_car = Car(model="GT-R")
# print(my_car.make)


from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

## label
label = Label(text="I am a Label", font=("Arial", 24, "bold"))
label["text"] = "My new text"
label.config(text="new text")
label.place(x=0, y=0)

## button
def button_clicked():
    label.config(text=input.get())

button = Button(text="Click Me", command=button_clicked)
button.config(padx=10, pady=10)
button.grid(column=0, row=0)

## Entry
input = Entry(width=30)
input.insert(END, string="Some text to begin with.")
input.grid(column=1, row=1)

## Textbox
text = Text(height=5, width=30)
# put cursor in textbox
text.focus()
# adds some text to begin with
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(column=0, row=3)

## Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

## Scale
## called with current scale value
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

## checkbutton
def checkbutton_used():
    # prints 1 if 0n button checked, otherwise 0.
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?",
                          variable=checked_state,
                          command=checkbutton_used)
checked_state.get()
# checkbutton.pack()

## Radiobutton
def radio_used():
    print(radio_state.get())
# variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

## Listbox
def listbox_used(event):
    # gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

window.mainloop()












